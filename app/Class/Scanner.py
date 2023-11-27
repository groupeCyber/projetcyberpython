from scapy import *

class Scanner:
    def __init__(self, interface):
        self.interface = interface
        self.packets = []

    def scan(self):
        while True:
            self.packets.append(sniff(iface=self.interface, count=1))
            yield self.packets
