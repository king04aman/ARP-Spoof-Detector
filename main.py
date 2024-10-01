import scapy.all as scapy
import time

def get_mac(ip):
    """Get the MAC address of a given IP."""
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    if answered_list:
        return answered_list[0][1].hwsrc
    else:
        return None

def detect_arp_spoof(target_ip, gateway_ip):
    """Detect ARP spoofing by monitoring ARP responses."""
    print("Starting ARP Spoof Detection...")
    try:
        while True:
            target_mac = get_mac(target_ip)
            gateway_mac = get_mac(gateway_ip)

            if not target_mac or not gateway_mac:
                print("Failed to retrieve MAC address. Exiting...")
                break

            arp_response = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=gateway_ip)

            if target_mac != gateway_mac:
                print("[ALERT] ARP Spoofing detected!")
                print(f"Gateway MAC: {gateway_mac}, Target MAC: {target_mac}")

            time.sleep(5)
    except KeyboardInterrupt:
        print("Stopping ARP Spoof Detector.")

if __name__ == "__main__":
    target_ip = input("Enter the target IP address: ")
    gateway_ip = input("Enter the gateway IP address: ")
    detect_arp_spoof(target_ip, gateway_ip)
