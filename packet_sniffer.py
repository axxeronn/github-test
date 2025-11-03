import socket
from scapy.all import *
from scapy.layers.l2 import Ether

sniffer_sockets = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))

interface = "eth0" 
sniffer_sockets.bind((interface, 0))

try:
    while True:
        raw_data, addr = sniffer_sockets.recvfrom(65565)
        packet = Ether(raw_data)
        print(packet.summary())
except KeyboardInterrupt:
    sniffer_sockets.close()        
