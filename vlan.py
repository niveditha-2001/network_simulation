from scapy.all import Ether, Dot1Q, sendp
from utils import get_interface

def send_vlan_frame(src_mac, dst_mac, vlan_name):
    iface = get_interface()
    vlan_id = 10 if vlan_name == "VLAN10" else 20  # Example VLAN logic
    
    frame = Ether(src=src_mac, dst=dst_mac) / Dot1Q(vlan=vlan_id) / b"Hello VLAN!"
    print(f"Sending VLAN {vlan_id} frame from {src_mac} to {dst_mac} on {iface}")
    sendp(frame, iface=iface, verbose=False)
