# ARP Spoof Detector

An **ARP Spoof Detector** written in Python to identify ARP spoofing attacks on a local network. The program uses the Scapy library to monitor ARP packets and detect anomalies indicating a potential attack.

## Features

- Monitors ARP packets on the local network.
- Detects potential ARP spoofing attempts.
- Logs suspicious activity for further investigation.
- Easy to use with simple Python scripts.

## Prerequisites

- Python 3.x
- Scapy library (`pip install scapy`)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/king04aman/arp-spoof-detector.git
   cd arp-spoof-detector
    ```
2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
### Usage
Run the program with superuser privileges:
```
sudo python main.py
```

### Example Output
```
[*] Listening for ARP packets...
[!] Possible ARP Spoofing detected!
    Source MAC: 00:11:22:33:44:55
    Destination MAC: 66:77:88:99:AA:BB
```
### License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Contribution
Contributions are welcome! Please open an issue or submit a pull request.

### Disclaimer
This program is intended for educational and research purposes only. Ensure you have permission before using it on any network.

