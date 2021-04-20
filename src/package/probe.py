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
import time

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
        self.result_operation_system_list = collections.deque()

        # class value
        self.probe_key = 0

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
        self.result_operation_system_list = collections.deque()

        # class value
        self.probe_key = 0

        return

    """ probe class main engine function
    @:param
        traceroute target protocol address
        traceroute max ttl
        traceroute verbose
        traceroute timeout
    @:returns
        deque :: protocol address list
        deque :: protocol address location list
    """
    def probe_engine(self, _traceroute_target_protocol_address, _traceroute_max_ttl,
                         _traceroute_verbose, _traceroute_timeout):
        self.reset_value()
        self.probe_set_traceroute_target_protocol_address(_traceroute_target_protocol_address)
        self.probe_set_traceroute_max_ttl(_traceroute_max_ttl)
        self.probe_set_traceroute_verbose(_traceroute_verbose)
        self.probe_set_traceroute_timeout(_traceroute_timeout)
        self.result_total_node_count, self.result_protocol_address_list = \
            self.probe_traceroute(self.probe_get_traceroute_target_protocol_address(),
                                  self.probe_get_traceroute_max_ttl(),
                                  self.probe_get_traceroute_verbose(),
                                  self.probe_get_traceroute_timeout())
        return self.probe_get_result()

    """ probe traceroute function
    @:param
        traceroute target protocol address
        traceroute max ttl
        traceroute verbose
        traceroute timeout
    @:return
        deque :: protocol address list
    """
    def probe_traceroute(self, _traceroute_target_protocol_address, _traceroute_max_ttl,
                         _traceroute_verbose, _traceroute_timeout):
        protocol_address_list = collections.deque()
        operation_system_list = collections.deque()

        total_node_count = 0
        for current_ttl_value in range(1, _traceroute_max_ttl):
            total_node_count = total_node_count + 1
            send_packet = IP(dst = _traceroute_target_protocol_address, ttl = current_ttl_value) / ICMP()
            response_packet = sr1(send_packet, verbose = _traceroute_verbose, timeout = _traceroute_timeout)

            if response_packet is not None:
                if response_packet.type == 0:  # icmp echo reply
                    protocol_address_list.append(response_packet.getlayer(IP).src)
                    operation_system_list.append(self.probe_operation_system(response_packet.getlayer(IP).ttl,
                                                                             total_node_count))
                    break
                else:
                    protocol_address_list.append(response_packet.getlayer(IP).src)
                    operation_system_list.append(self.probe_operation_system(response_packet.getlayer(IP).ttl,
                                                                             total_node_count))

        return total_node_count, protocol_address_list

    """ probe node location function
    @:param
        deque :: protocol address list
    @:return
        deque :: protocol address location list
    @:api
        http://ip-api.com/json/
    """
    def probe_node_location(self, _protocol_address_list = collections.deque()):
        """ probe_node_location function's value.
         api_url : using api's url address
         protocol_address : ip address
         headers : http (tcp/80) request header
        """
        location_list = collections.deque()

        for i in range(0, self.result_total_node_count):
            try:
                api_url = "http://ip-api.com/json/"
                protocol_address = _protocol_address_list[i]
                headers = {
                    ""
                }
                response = requests.get(url = api_url + protocol_address, headers = headers)
                json_response = response.json()
                location_list.append(json_response["country"])
            except ConnectionResetError:
                pass

            time.sleep(0.5)

        return location_list

    """ probe operation system function
    @:param
        time to live value (ttl)
        
    @:return
        ??
    """
    def probe_operation_system(self, _time_to_live, _hop_count):
        server_time_to_live = _time_to_live + _hop_count # icmp response ttl is os ttl - hop count
        if (server_time_to_live >= 62) and (server_time_to_live <= 65):
            # Linux Series Operation System
            return "Linux Series"
        elif (server_time_to_live >= 126) and (server_time_to_live <= 129):
            # Windows Series Operation System
            return "Windows Series"
        elif (server_time_to_live >= 254) and (server_time_to_live <= 257):
            # Cisco Series Operation System
            return "Cisco Series"
        else:
            return "null"

    """ get result function
    @:returns
        protocol address list
        location list
        total node count
    """
    def probe_get_result(self):
        return self.result_protocol_address_list, self.result_operation_system_list, \
               self.result_location_list, self.result_total_node_count

    """ probe demo function
    """
    def probe_demo(self, _traceroute_target_protocol_address, _traceroute_max_ttl,
                         _traceroute_verbose, _traceroute_timeout):
        self.reset_value()
        self.probe_set_traceroute_target_protocol_address(_traceroute_target_protocol_address)
        self.probe_set_traceroute_max_ttl(_traceroute_max_ttl)
        self.probe_set_traceroute_verbose(_traceroute_verbose)
        self.probe_set_traceroute_timeout(_traceroute_timeout)
        self.result_total_node_count, self.result_protocol_address_list = \
            self.probe_traceroute(self.probe_get_traceroute_target_protocol_address(),
                                  self.probe_get_traceroute_max_ttl(),
                                  self.probe_get_traceroute_verbose(),
                                  self.probe_get_traceroute_timeout())
        return self.probe_get_result_protocol_address_list(), self.probe_get_result_operation_system_list() # ip list, os result

    """ set-get zone
    
    """
    def probe_set_traceroute_target_protocol_address(self, _traceroute_target_protocol_address):
        self.traceroute_target_protocol_address = _traceroute_target_protocol_address
        return

    def probe_set_traceroute_max_ttl(self, _traceroute_max_ttl):
        self.traceroute_max_ttl = _traceroute_max_ttl
        return

    def probe_set_traceroute_verbose(self, _traceroute_verbose):
        self.traceroute_verbose = _traceroute_verbose
        return

    def probe_set_traceroute_timeout(self, _traceroute_timeout):
        self.traceroute_timeout = _traceroute_timeout
        return

    def probe_get_traceroute_target_protocol_address(self):
        return self.traceroute_target_protocol_address

    def probe_get_traceroute_max_ttl(self):
        return self.traceroute_max_ttl

    def probe_get_traceroute_verbose(self):
        return self.traceroute_verbose

    def probe_get_traceroute_timeout(self):
        return self.traceroute_timeout

    def probe_get_result_total_node_count(self):
        return self.result_total_node_count

    def probe_get_result_protocol_address_list(self):
        return self.result_protocol_address_list

    def probe_get_result_location_list(self):
        return self.result_location_list

    def probe_get_result_operation_system_list(self):
        return self.result_operation_system_list

