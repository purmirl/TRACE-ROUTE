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

import collections

class Probe():

    def __init__(self):
        # traceroute parameter value
        self.traceroute_min_ttl = 1
        self.traceroute_max_ttl = 22
        self.traceroute_verbose = 0
        self.traceroute_target_protocol_address = ""

        # traceroute result value
        self.result_total_node_count = 0
        self.result_protocol_address_list = collections.deque()

        # class valuu
        self.probe_key = 0


        self.probe_engine_exception_key = 0
        self.probe_engine_icmp_hit_count = 0
        self.probe_engine_icmp_ttl_count = 1 # important

        self.traget_protocol_address = ""

        self.protocol_adrress_list = collections.deque()
        return

    def reset_value(self):
        self.probe_engine_exception_key = 0
        self.probe_engine_icmp_hit_count = 0
        self.probe_engine_icmp_ttl_count = 1
        self.probe_engine_min_icmp_ttl = 1
        self.probe_engine_max_icmp_ttl = 22

        self.traget_protocol_address = ""

        self.protocol_adrress_list.clear()
        return

    def probe_engine(self, _protocol_address):

        # while True:

        return

    def probe_traceroute_get_result_ip(self):

        return

