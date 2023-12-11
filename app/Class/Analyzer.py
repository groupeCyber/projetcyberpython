from Class.Scanner import Scanner
from Class.Alerter import Alerter
from scapy.all import *
import logging

class Analyzer:
    def __init__(self, interface, token, email):
        self.logger = logging.getLogger('global')
        self.scanner = Scanner(interface)
        self.alerter = Alerter(token, email)

    def get_packet_data(self, range):
        scan  = self.scanner.scan()
        packets = []
        for packet in scan:
            print('Packet recieved')
            packets.append(packet[0])
            if len(packets) >= range:
                print(f'{range} packets achieved')
                self.analyze(packets)
                packets = []

    def analyze(self, packets):
        pings = self.ping_detection(packets)
        ports = self.port_scan_detection(packets)
        if pings: self.alerter.send_alert('Ping alert', f'Pings detected, see the following list :\n\n{pings}')
        if ports: self.alerter.send_alert('Port scan alert', f'Port scans detected, see the following list :\n\n{ports}')

    def ping_detection(self, packets):
        pings = []
        for packet in packets:
            if ICMP in packet:
                info = f'Ping detected from {packet[IP].src} to {packet[IP].dst}'
                pings.append(info)
                self.logger.warning(info)
                print(info)
        return pings if len(pings) > 3 else False

    def port_scan_detection(self, packets):
        src_ip_to_ports = {}
        suspicious = []
        for packet in packets:
            if TCP in packet or UDP in packet:
                src_ip = packet[IP].src
                dst_port = packet[TCP].dport if TCP in packet else packet[UDP].dport
                src_ip_to_ports.setdefault(src_ip, set()).add(dst_port)
        for src_ip, ports in src_ip_to_ports.items():
            if len(ports) >= 1:
                info = f"Port scan detected from {src_ip} to {ports}"
                suspicious.append(info)
                self.logger.warning(info)
                print(info)
        return suspicious if len(suspicious) > 0 else False