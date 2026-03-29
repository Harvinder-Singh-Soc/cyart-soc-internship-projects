# ELK Stack Setup Commands (Lab Notes)

> Lab host: `ELK-SERVER` (Linux Mint).  
> Purpose: SIEM backend for Day 05 SOC lab.

## 1. Basic OS Prep and Hostname

```bash
sudo su -
hostnamectl set-hostname ELK-SERVER

echo "your ip ELK-SERVER elk" >> /etc/hosts
cat /etc/hosts

apt update
apt install -y gnupg2 apt-transport-https curl default-jdk vim nano git net-tools
ifconfig

shutdown -r now
sudo apt update -y
```

## 2. Elasticsearch 9.x Install and Config

```bash
# Add Elastic GPG key and repo
wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | \
  gpg --dearmor -o /etc/apt/trusted.gpg.d/elastic.gpg

echo "deb https://artifacts.elastic.co/packages/9.x/apt stable main" \
  > /etc/apt/sources.list.d/elastic-9.x.list

apt update
apt install -y elasticsearch
```

```bash
# Check non-comment config
grep -Ev '^#|^$' /etc/elasticsearch/elasticsearch.yml
```

```bash
# JVM heap (adjust for your RAM)
cat <<EOF > /etc/elasticsearch/jvm.options.d/jvm-heap.options
-Xms4g
-Xmx4g
EOF
```

```bash
# Backup config then open ES to the lab network
cp /etc/elasticsearch/elasticsearch.yml /etc/elasticsearch/elasticsearch.yml.bak

sed -i 's/#network.host: 192.168.0.1/network.host: 0.0.0.0/' /etc/elasticsearch/elasticsearch.yml
sed -i 's/#transport.host: 0.0.0.0/transport.host: 0.0.0.0/' /etc/elasticsearch/elasticsearch.yml
```

```bash
# Enable and verify ES
systemctl daemon-reload
systemctl enable --now elasticsearch
systemctl status elasticsearch

ss -altnp | grep -E "9200|9300"
```

```bash
# Reset Elastic user password (interactive)
# NOTE: in lab I set a simple password; in docs use a placeholder
/usr/share/elasticsearch/bin/elasticsearch-reset-password -u elastic -i
# -> set to <ELASTIC_PASSWORD>
```

```bash
# Test HTTPS API
curl https://ELK-SERVER:9200 \
  --cacert /etc/elasticsearch/certs/http_ca.crt \
  -u elastic:<ELASTIC_PASSWORD>
```

## 3. Kibana Install and Config

```bash
apt install -y kibana
cp /etc/kibana/kibana.yml /etc/kibana/kibana_backup.yml

sed -i 's/#server.port: 5601/server.port: 5601/' /etc/kibana/kibana.yml
sed -i 's/#server.host: "localhost"/server.host: "0.0.0.0"/' /etc/kibana/kibana.yml
```

```bash
# Generate and set encryption keys (replace with your generated values)
#/usr/share/kibana/bin/kibana-encryption-keys generate

cat <<EOF >> /etc/kibana/kibana.yml
xpack.encryptedSavedObjects.encryptionKey: <ENCRYPTED_OBJECTS_KEY>
xpack.reporting.encryptionKey: <REPORTING_KEY>
xpack.security.encryptionKey: <SECURITY_KEY>
EOF

grep -Ev '^#|^$' /etc/kibana/kibana.yml
```

```bash
systemctl daemon-reload
systemctl enable --now kibana
systemctl status kibana

ss -altnp | grep 5601
```

```bash
# Generate Kibana enrollment token (paste into browser UI when first logging in)
/usr/share/elasticsearch/bin/elasticsearch-create-enrollment-token -s kibana

# Optional: Kibana verification code
/usr/share/kibana/bin/kibana-verification-code
```

## 4. Logstash (Optional for this lab)

```bash
apt install -y logstash

# Save ES CA cert for Logstash
openssl s_client -showcerts -connect ELK-SERVER:9200 </dev/null 2>/dev/null \
  | openssl x509 > /etc/logstash/elasticsearch-ca.crt

systemctl daemon-reload
systemctl enable --now logstash
systemctl status logstash

tail -f /var/log/logstash/logstash-plain.log
ss -altnp | grep 5044
```

## 5. Filebeat Example (before switching to Elastic Agent)

```bash
apt install -y filebeat
cp /etc/filebeat/filebeat.yml /etc/filebeat/filebeat_backup.yml
```

```bash
telnet ELK-SERVER 9200 || nc -vz ELK-SERVER 9200
```

```bash
nano /etc/filebeat/filebeat.yml
# Example minimal config:
# - type: filestream
#   id: my-filestream-id
#   enabled: true
#   paths:
#     - /var/log/*.log
#     - /var/log/syslog
# setup.kibana:
#   host: "ELK-SERVER:5601"
# output.elasticsearch:
#   hosts: ["ELK-SERVER:9200"]
#   protocol: "https"
#   ssl.certificate_authorities: ["/etc/elasticsearch/certs/http_ca.crt"]
#   username: "elastic"
#   password: "<ELASTIC_PASSWORD>"
```

```bash
filebeat test config -e
filebeat modules list
filebeat modules enable system
sed -i '/enabled:/s/false/true/' /etc/filebeat/modules.d/system.yml

filebeat setup -e

systemctl daemon-reload
systemctl enable --now filebeat
systemctl restart filebeat
systemctl status filebeat
```
## 6. Elastic Agent + Fleet (Final SIEM Setup)

In the final version of the lab I stopped using Filebeat and moved to **Elastic Agent + Fleet**, so that all log collection is managed centrally from Kibana.

### 6.1 Fleet Server on ELK-SERVER

```bash
# Download Elastic Agent (version must match Elasticsearch/Kibana)
cd /tmp
curl -L -O https://artifacts.elastic.co/downloads/beats/elastic-agent/elastic-agent-<VERSION>-linux-x86_64.tar.gz
tar xzvf elastic-agent-<VERSION>-linux-x86_64.tar.gz
cd elastic-agent-<VERSION>-linux-x86_64
```

```bash
# Install Elastic Agent as Fleet Server (policy: ELK-fleet-server-policy)
sudo ./elastic-agent install \
  --url=https://ELK-SERVER:8220 \
  --enrollment-token=<FLEET_SERVER_ENROLLMENT_TOKEN> \
  --fleet-server-es=https://ELK-SERVER:9200 \
  --fleet-server-policy=ELK-fleet-server-policy
```

After installation, the agent on **ELK-SERVER** appears in Kibana Fleet under the policy `ELK-fleet-server-policy` and shows status **Healthy**.

### 6.2 Elastic Agent on mint-victim (logs + auth)

On the **mint-victim** VM, Elastic Agent is installed as a normal endpoint agent and attached to a dedicated policy for system logs and SSH authentication.

```bash
# Download and extract Elastic Agent
cd /tmp
curl -L -O https://artifacts.elastic.co/downloads/beats/elastic-agent/elastic-agent-<VERSION>-linux-x86_64.tar.gz
tar xzvf elastic-agent-<VERSION>-linux-x86_64.tar.gz
cd elastic-agent-<VERSION>-linux-x86_64
```

```bash
# Enroll agent into Fleet using mint-system-policy
sudo ./elastic-agent install \
  --url=https://ELK-SERVER:8220 \
  --enrollment-token=<MINT_SYSTEM_POLICY_ENROLLMENT_TOKEN>
```

In Kibana Fleet:

- The agent on mint-victim is attached to the policy **`mint-system-policy`**.  
- The policy enables the **System** integration with:
  - `system` (System logs dataset)  
  - `system/auth` (System auth dataset for SSH login events)

Once the agent status is **Healthy**, `logs-system.auth*` and related indices start receiving sshd events with parsed fields such as `source.ip`, `user.name`, `event.outcome`, `host.name`, and `process.name`.