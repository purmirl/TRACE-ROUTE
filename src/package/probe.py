"""
 Copyright 2020~ PeTrA. All rights reserved.
 . Python Project Structure Repository;

 Probe Arrow Project (Advanced Trace Route) by PeTrA. 2020~
 ProbeArrow 1.0
 Language : Python3.8.2 on pycharm IDE
 Library : Scapy2.4.3
 API : IP Geo Location [geoplugin.net] --> http://www.geoplugin.net/json
 ------
 @ main.py
    * ProbeArrow/src/package/probe.py
    * probe (trace route module) code file
"""

import collections
import json
from urllib.request import urlopen
from scapy.layers.inet import IP, ICMP
from scapy.sendrecv import sr1
from src.package.function import is_protocol_address

""" @Probe class
"""
class Probe:
    def __init__(self):
        self.reset_value()
        return

    """ @reset class value
    """
    def reset_value(self):
        # traceroute parameter value
        self.traceroute_target_protocol_address = ""
        self.traceroute_max_ttl = 40
        self.traceroute_verbose = 0
        self.traceroute_timeout = 3
        self.traceroute_interface = ""

        # traceroute result value
        self.result_total_node_count = 0
        self.result_protocol_address_list = collections.deque()
        self.result_location_list = collections.deque()
        self.result_operation_system_list = collections.deque()
        self.result_server_ttl_list = collections.deque()

        # class value
        self.probe_key = 0
        return

    """ @probe class main engine function
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
                     _traceroute_verbose, _traceroute_timeout, _traceroute_interface):
        self.reset_value()
        self.probe_set_traceroute_target_protocol_address(_traceroute_target_protocol_address)
        self.probe_set_traceroute_max_ttl(_traceroute_max_ttl)
        self.probe_set_traceroute_verbose(_traceroute_verbose)
        self.probe_set_traceroute_timeout(_traceroute_timeout)
        self.probe_set_traceroute_interface(_traceroute_interface)
        self.result_total_node_count, self.result_protocol_address_list, self.result_operation_system_list, self.result_server_ttl_list, self.result_location_list = self.probe_traceroute(self.probe_get_traceroute_target_protocol_address(),
                                  self.probe_get_traceroute_max_ttl(),
                                  self.probe_get_traceroute_verbose(),
                                  self.probe_get_traceroute_timeout(),
                                  self.probe_get_traceroute_interface())
        return self.probe_get_result_protocol_address_list(), self.probe_get_result_operation_system_list(), \
               self.probe_get_result_total_node_count(), self.probe_get_result_location_list(), self.probe_get_result_server_ttl_list()

    """ @probe traceroute function
    @:param
        traceroute target protocol address
        traceroute max ttl
        traceroute verbose
        traceroute timeout
    @:return
        deque :: protocol address list
    """
    def probe_traceroute(self, _traceroute_target_protocol_address, _traceroute_max_ttl,
                         _traceroute_verbose, _traceroute_timeout, _traceroute_interface):
        protocol_address_list = collections.deque()
        operation_system_list = collections.deque()
        server_ttl_list = collections.deque()
        total_node_count = 0
        for current_ttl_value in range(1, _traceroute_max_ttl + 1):
            total_node_count = total_node_count + 1
            send_packet = IP(dst=_traceroute_target_protocol_address, ttl=current_ttl_value) / ICMP()
            response_packet = sr1(send_packet, verbose=_traceroute_verbose, timeout=_traceroute_timeout, iface=_traceroute_interface)

            if response_packet is not None:
                if response_packet.type == 0:  # icmp echo reply
                    protocol_address_list.append(response_packet.getlayer(IP).src)
                    operation_system, server_ttl = self.probe_operation_system(response_packet.getlayer(IP).ttl,
                                                                             total_node_count)
                    operation_system_list.append(operation_system)
                    server_ttl_list.append(server_ttl)
                    break
                else:
                    protocol_address_list.append(response_packet.getlayer(IP).src)
                    operation_system, server_ttl = self.probe_operation_system(response_packet.getlayer(IP).ttl,
                                                                             total_node_count)
                    operation_system_list.append(operation_system)
                    server_ttl_list.append(server_ttl)
            else:
                protocol_address_list.append("Unknown")
                operation_system_list.append("Unknown")
                server_ttl_list.append("Unknown")
        return total_node_count, protocol_address_list, operation_system_list, server_ttl_list, \
               self.probe_node_location(total_node_count, protocol_address_list)

    """ @probe node location function
    @:param
        deque :: protocol address list
    @:return
        deque :: protocol address location list
    @:api
        http://www.geoplugin.net/
    """
    def probe_node_location(self, _total_node_count, _protocol_address_list=collections.deque()):
        """ @probe_node_location function's value.
         api_url : using api's url address
         protocol_address : ip address
         headers : http (tcp/80) request header
        """
        location_list = collections.deque()
        for i in range(0, _total_node_count):
            protocol_address = _protocol_address_list[i]
            is_ip_address = is_protocol_address(protocol_address)
            if is_ip_address == 1:
                try:
                    api_url = "http://www.geoplugin.net/json.gp?ip="
                    url = api_url + protocol_address
                    response = urlopen(url)
                    data = json.load(response)
                    location_string = str(data["geoplugin_countryName"])
                    if location_string == "None":
                        location_list.append("Unknown")
                    else:
                        location_list.append(location_string)
                except: # ConnectionResetError
                    location_list.append("Unknown")
            else:
                location_list.append("403 Error")
        return location_list

    """ @probe operation system function
    @:param
        time to live value (ttl)
    @:return
        ??
    """
    def probe_operation_system(self, _time_to_live, _hop_count):
        server_time_to_live = _time_to_live + _hop_count  # icmp response ttl is os ttl - hop count
        if (server_time_to_live >= 62) and (server_time_to_live <= 65):
            # Linux Series Operation System
            return "Linux Series", server_time_to_live
        elif (server_time_to_live >= 58) and (server_time_to_live <= 61):
            return "Cisco Series", server_time_to_live
        elif (server_time_to_live >= 126) and (server_time_to_live <= 129):
            # Windows Series Operation System
            return "Windows Series", server_time_to_live
        elif (server_time_to_live >= 254) and (server_time_to_live <= 257):
            # Cisco Series Operation System
            return "Cisco Series", server_time_to_live
        else:
            return "Unknown", server_time_to_live

    """ @get result function
    @:returns
        protocol address list
        location list
        total node count
    """
    def probe_get_result(self):
        return self.result_protocol_address_list, self.result_operation_system_list, \
               self.result_location_list, self.result_total_node_count, self.result_server_ttl_list

    """ @probe engine demo function. back up - 20210516
    def probe_demo(self, _traceroute_target_protocol_address, _traceroute_max_ttl,
                   _traceroute_verbose, _traceroute_timeout):
        self.reset_value()
        self.probe_set_traceroute_target_protocol_address(_traceroute_target_protocol_address)
        self.probe_set_traceroute_max_ttl(_traceroute_max_ttl)
        self.probe_set_traceroute_verbose(_traceroute_verbose)
        self.probe_set_traceroute_timeout(_traceroute_timeout)
        self.result_total_node_count, self.result_protocol_address_list, self.result_operation_system_list = \
            self.probe_traceroute(self.probe_get_traceroute_target_protocol_address(),
                                  self.probe_get_traceroute_max_ttl(),
                                  self.probe_get_traceroute_verbose(),
                                  self.probe_get_traceroute_timeout())
        return self.probe_get_result_protocol_address_list(), self.probe_get_result_operation_system_list(), \
               self.result_total_node_count  # ip list, os result
    """

    """ @set-get zone
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

    def probe_set_traceroute_interface(self, _traceroute_interface):
        self.traceroute_interface = _traceroute_interface

    def probe_get_traceroute_target_protocol_address(self):
        return self.traceroute_target_protocol_address

    def probe_get_traceroute_max_ttl(self):
        return self.traceroute_max_ttl

    def probe_get_traceroute_verbose(self):
        return self.traceroute_verbose

    def probe_get_traceroute_timeout(self):
        return self.traceroute_timeout

    def probe_get_traceroute_interface(self):
        return self.traceroute_interface

    def probe_get_result_total_node_count(self):
        return self.result_total_node_count

    def probe_get_result_protocol_address_list(self):
        return self.result_protocol_address_list

    def probe_get_result_location_list(self):
        return self.result_location_list

    def probe_get_result_operation_system_list(self):
        return self.result_operation_system_list

    def probe_get_result_server_ttl_list(self):
        return self.result_server_ttl_list