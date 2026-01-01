import subprocess
import re

def scan_wifi():
    command = ["netsh", "wlan", "show", "networks", "mode=Bssid"]
    output = subprocess.check_output(command, encoding="utf-8", errors="ignore")

    networks = []
    current = {}

    for line in output.split("\n"):
        line = line.strip()

        if line.startswith("SSID"):
            if current:
                networks.append(current)
            current = {}

        if "Signal" in line:
            signal = int(re.search(r"(\d+)%", line).group(1))
            current["rssi"] = -100 + signal

        if "Radio type" in line:
            current["freq"] = 2.4 if "802.11b" in line or "g" in line else 5.0

    if current:
        networks.append(current)

    return networks
