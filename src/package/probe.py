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

from pip._vendor import requests
from scapy.layers.inet import IP, ICMP
from scapy.sendrecv import sr1


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
        self.result_location_list = collections.deque()

        # class value
        self.probe_key = 0

        """
        self.probe_engine_exception_key = 0
        self.probe_engine_icmp_hit_count = 0
        self.probe_engine_icmp_ttl_count = 1 # important

        self.traget_protocol_address = ""

        self.protocol_adrress_list = collections.deque()
        """
        return

    def reset_value(self):
        # traceroute parameter value
        self.traceroute_target_protocol_address = ""
        self.traceroute_max_ttl = 40
        self.traceroute_verbose = 0
        self.traceroute_timeout = 3

        # traceroute result value
        self.result_total_node_count = 0
        self.result_protocol_address_list = collections.deque()
        self.result_location_list = collections.deque()

        # class value
        self.probe_key = 0

        return

    def probe_engine(self, _protocol_address):

        # while True:

        return

    def probe_traceroute(self, _traceroute_target_protocol_address, _traceroute_max_ttl,
                         _traceroute_verbos, _traceroute_timeout):
        protocol_address_list = collections.deque()
        for current_ttl_value in range(1, _traceroute_max_ttl):
            print(current_ttl_value, " hop..")
            total_node_count = total_node_count + 1
            send_packet = IP(dst = _traceroute_target_protocol_address, ttl = current_ttl_value) / ICMP()
            response_packet = sr1(send_packet, verbose = _traceroute_verbos, timeout = _traceroute_timeout)

            if response_packet is not None:
                if response_packet.type == 0:  # icmp echo reply
                    print("finish !! " + response_packet.getlayer(IP).src)
                    protocol_address_list.append(response_packet.getlayer(IP).src)
                    break
                else:
                    print(response_packet.getlayer(IP).src)
                    protocol_address_list.append(response_packet.getlayer(IP).src)


        # traceroute result check area
        # print("result_total_node_count = ", total_node_count)
        # print("result_protocol_address_list", protocol_address_list)

        return total_node_count, protocol_address_list

    def probe_node_location(self, _protocol_address_list = collections.deque()):
        # probe_node_location function's value.
        #     api_url : using api's url address
        #     protocol_address : ip address
        #     headers : http (tcp/80) request header
        api_url = ""
        protocol_address = ""
        headers = {
            ""
        }
        try:
            response = requests.get(url = api_url + protocol_address, headers = headers)
        except ConnectionResetError:
            pass

        return

"""
    def probe_traceroute_get_result_ip(self):

        return
"""

