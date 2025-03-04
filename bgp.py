from scapy.all import IP, sendp
from utils import get_interface

def send_bgp_update():
    iface = get_interface()
    packet = IP(dst="192.168.1.1") / b"BGP Update"
    print(f"Sending BGP Update on {iface}")
    sendp(packet, iface=iface, verbose=False)
