from scapy.all import *
import time

class Scanner:
    def __init__(self, interface):
        self.interface = interface

    def scan(self):
        while True:
            packets = (sniff(iface=self.interface, count=10))
            self.logging(packets)
            yield packets

    def logging(self, packets):
        for packet in packets:
            log_entry = self.processing_packet(packet)
            with open("logs/general_logs.txt", "a") as log_file:
                log_file.write(log_entry)
    
    def processing_packet(self, packet):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        src_ip, dst_ip = None, None
        if IP in packet:
            src_ip = packet[IP].src
            dst_ip = packet[IP].dst
        src_port, dst_port, proto = None, None, None
        if TCP in packet:
            print(packet[TCP])
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
            proto = "TCP"
        elif UDP in packet:
            print(packet[UDP])
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport
            proto = "UDP"
        elif ICMP in packet:
            proto = "ICMP"
            src_port, dst_port = "-", "-"
        return f"{timestamp} | Protocol: {proto} | Source IP: {src_ip} | Destination IP: {dst_ip} | Source Port: {src_port} | Destination Port: {dst_port}\n"