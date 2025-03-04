from scapy.all import IP, sendp
from utils import get_interface

def send_ospf_hello():
    iface = get_interface()
    packet = IP(dst="224.0.0.5") / b"OSPF Hello"
    print(f"Sending OSPF Hello on {iface}")
    sendp(packet, iface=iface, verbose=False)
