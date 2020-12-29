"""
 Copyright 2020~ PeTrA. All rights reserved.
 . Python Project Structure Repository;

 Probe Arrow Project by PeTrA. 2020
 ProbeArrow 1.0
 Language : Python3.8.2
 Library : Scapy2.4.3

 Advanced Trace Route
 ------
 @ probe.py
    * probe function code file
"""

# ProbeArrow/src/probe.py;

class Probe():

    def __init__(self):
        self.probe_engine_exception_key = 0
        self.probe_engine_icmp_hit_count = 0
        self.probe_engine_icmp_ttl_count = 1 # important
        self.probe_engine_min_icmp_ttl = 1
        self.probe_engine_max_icmp_ttl = 22


        return

    def probe_engine(self, _protocol_address):

        # while True:

        return