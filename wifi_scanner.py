import time
from datetime import datetime

def scan_wifi():
    # Simulated output for testing in VM
    fake_output = """
MyWiFiNetwork:75
HiddenNetwork:20
CafeteriaNet:50
SlowCafe:30
"""

    networks = fake_output.strip().split('\n')
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("wifi_log.txt", "a") as log:
        for net in networks:
            ssid, signal = net.split(":")
            print(f"[{timestamp}] SSID: {ssid}, Signal: {signal}")
            log.write(f"[{timestamp}] SSID: {ssid}, Signal: {signal}\n")
            if int(signal) < 40:
                print(f" Weak signal detected: {ssid} ({signal})")

if __name__ == "__main__":
    while True:
        scan_wifi()
        print("=" * 40)
        time.sleep(10)


