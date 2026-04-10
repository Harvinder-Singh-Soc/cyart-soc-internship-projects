@echo off
REM =============================================
REM SOC Lab - Firewall Block Rule
REM Blocks inbound traffic from attacker IP
REM =============================================

set ATTACKER_IP=192.168.56.133
set RULE_NAME=Block_BruteForce_Attacker

echo Creating firewall rule to block %ATTACKER_IP%...
netsh advfirewall firewall add rule name="%RULE_NAME%" dir=in action=block remoteip=%ATTACKER_IP% enable=yes

if %ERRORLEVEL% EQU 0 (
    echo [SUCCESS] Rule "%RULE_NAME%" added successfully.
) else (
    echo [ERROR] Failed to add rule. Run as Administrator.
)

echo.
echo Verifying rule...
netsh advfirewall firewall show rule name="%RULE_NAME%"

pause