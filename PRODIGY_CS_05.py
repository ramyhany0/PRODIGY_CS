from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP

def packet_callback(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        protocol = packet[IP].proto

        if protocol == 6:
            proto = "TCP"
        elif protocol == 17:
            proto = "UDP"
        else:
            proto = "Other"

        print(f"Source: {ip_src} -> Destination: {ip_dst} | Protocol: {proto}")

        # Display payload data for TCP/UDP packets
        if proto in ["TCP", "UDP"]:
            payload = bytes(packet[IP].payload)
            print(f"Payload: {payload}\n")

def main():
    print("Starting packet capture...")
    sniff(prn=packet_callback, store=False)

if __name__ == "__main__":
    main()
