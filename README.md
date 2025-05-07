# Wi-FI Scanner (simulated)
A simulated Python script that mimics real-time Wi-Fi scanning for testing and QA logging. Designed for environments where the guest OS can't access host wireless hardware (e.g., VMs).

## Features
 - Parses mock SSID/signal data
 - Logs enntries to 'wifi_log.txt'
 - Warns on weak signal @ <40
 - Runs continuously every 10 seconds

## Files
 - 'wifi_scanner.py' - main Python script
 - 'wifi_log.txt' - generated log file
 
## How to Run
'''
bash
python3 wifi_scanner.py
'''
