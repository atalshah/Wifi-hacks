from pywifi import PyWiFi, const, Profile
import time

wifi = PyWiFi()
iface = wifi.interfaces()[0]

def scan_wifi():
    iface.scan()
    time.sleep(2)
    results = iface.scan_results()
    for result in results:
        print(f"SSID: {result.ssid}, Signal: {result.signal}")

scan_wifi()