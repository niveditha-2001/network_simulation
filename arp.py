from scapy.all import ARP, Ether, srp
from utils import get_interface

def send_arp_request(target_ip):
    iface = get_interface()
    arp_request = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=target_ip)
    response, _ = srp(arp_request, timeout=2, verbose=False, iface=iface)
    
    for _, received in response:
        print(f"ARP Reply: {received.psrc} is at {received.hwsrc}")