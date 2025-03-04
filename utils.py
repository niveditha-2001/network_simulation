from scapy.all import get_if_list, get_working_if

def get_interface():
    """Find a working network interface automatically."""
    iface = get_working_if()
    if iface is None:
        raise ValueError("No working network interface found!")
    return iface


def list_interfaces():
    """List all available network interfaces."""
    return get_if_list()
