from Class.Scanner import Scanner
from Class.Alerter import Alerter
from scapy.all import *
import time

class Analyzer:
    def __init__(self, interface):
        self.scanner = Scanner(interface)
        self.alerter = Alerter('khsdfjhldsjf','test@test.com')

    def get_packet_data(self, range):
        scan  = self.scanner.scan()
        packets = []
        for packet in scan:
            print('Packet recieved')
            packets.append(packet)
            if len(packets) >= range:
                print(f'{range} packets achieved')
                self.analyze(packets)
                packets = []

    def analyze(self, packets):
        pings = self.ping_detection(packets)
        ports = self.port_scan_detection(packets)
        if pings:
            for ping in pings:
                print('Ping detected', ping)
                self.alerter.send_alert('Ping detected', ping)
        if ports:
            self.alerter.send_alert('Port scan detected', ports)

    def ping_detection(self, packets):
        pings = []
        for packet in packets:
            print('Packet', packet)
            if ICMP in packet:
                print('ICMP packet detected')
                pings.append(f"ICMP packet detected from {packet[IP].src} to {packet[IP].dst}")
            print('Pings', pings)
        return pings if len(pings) > 5 else False

    def port_scan_detection(self, packets):
        src_ip_to_ports = {}
        for packet in packets:
            if TCP in packet or UDP in packet:
                src_ip = packet[IP].src
                dst_port = packet[TCP].dport if TCP in packet else packet[UDP].dport
                src_ip_to_ports.setdefault(src_ip, set()).add(dst_port)
        
        for src_ip, ports in src_ip_to_ports.items():
            if len(ports) > 5:
                return f"Port scan detected from {src_ip} to {ports}"
        return False