from scapy.all import IP, ICMP, sr1

def send_ping(target_ip):
    packet = IP(dst=target_ip) / ICMP()
    response = sr1(packet, timeout=2, verbose=False)
    
    if response:
        print(f"Ping reply from {response.src}: TTL={response.ttl}")
    else:
        print("Request timed out.")