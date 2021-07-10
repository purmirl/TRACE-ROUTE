"""
 Copyright 2020 PeTrA. All rights reserved.
 . Python Project Structure Repository;
"""
# PythonProjectStructre/tests/test_main.py;
from scapy.arch import IFACES
from scapy.layers.inet import IP, ICMP
from scapy.sendrecv import sr1



_iface = "Intel(R) Dual Band Wireless-AC 7265"

temp = IFACES.data.values()
temp = list(temp)
for i in range(0, len(temp)):
    print(temp[i])

send_packet = IP(dst="8.8.8.8", ttl=22) / ICMP()

response_packet = sr1(send_packet, verbose=22, timeout=22, iface="Intel(R) Dual Band Wireless-AC 7265")