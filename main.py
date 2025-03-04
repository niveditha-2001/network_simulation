from vlan import send_vlan_frame
from arp import send_arp_request
from icmp import send_ping
from ospf import send_ospf_hello
from bgp import send_bgp_update

def run_simulation():
    print("\n🔵 Running VLAN Simulation")
    send_vlan_frame("00:11:22:33:44:55", "FF:FF:FF:FF:FF:FF", "VLAN10")

    print("\n🔵 Running ARP Simulation")
    send_arp_request("192.168.1.1")

    print("\n🔵 Running ICMP Ping")
    send_ping("8.8.8.8")

    print("\n🔵 Running OSPF Simulation")
    send_ospf_hello()

    print("\n🔵 Running BGP Simulation")
    send_bgp_update()

if __name__ == "__main__":
    run_simulation()
