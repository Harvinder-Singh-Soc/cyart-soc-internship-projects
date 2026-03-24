import time
import requests

URLS = [
    "https://www.google.com",
    "https://www.youtube.com",
    "https://www.github.com",
    "https://www.python.org",
    "https://www.wikipedia.org",
]

def main() -> None:
    print("[*] Starting simple HTTPS traffic generator...")
    for i in range(3):  # 3 rounds
        print(f"\n[+] Round {i+1}")
        for url in URLS:
            try:
                print(f"  -> GET {url}")
                resp = requests.get(url, timeout=5)
                print(f"     Status: {resp.status_code}, length: {len(resp.content)}")
            except Exception as e:
                print(f"     Error: {e}")
            time.sleep(1)  # thoda gap for nicer packet timing
    print("\n[*] Done. Check Wireshark capture.")

if __name__ == "__main__":
    main()
