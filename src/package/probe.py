"""
 Copyright 2020~ PeTrA. All rights reserved.
 . Python Project Structure Repository;

 Probe Arrow Project (Advanced Trace Route) by PeTrA. 2020~
 ProbeArrow - version 2021.12.01
  . base of Python3.8.2 on pycharm IDE, Scapy2.4.3
  . using API : IP Geo Location [geoplugin.net] --> http://www.geoplugin.net/json
  . package is here --> https://github.com/purmirl/ProbeArrow


 @ main.py
    * ProbeArrow/src/package/probe.py
    * probe (trace route module) code file
"""

import collections
import json
import timeit
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
        """self.result_total_node_count, self.result_protocol_address_list, self.result_operation_system_list, self.result_server_ttl_list, self.result_location_list = """
        self.probe_traceroute(self.probe_get_traceroute_target_protocol_address(),
                                  self.probe_get_traceroute_max_ttl(),
                                  self.probe_get_traceroute_verbose(),
                                  self.probe_get_traceroute_timeout(),
                                  self.probe_get_traceroute_interface())
        return # self.probe_get_result_protocol_address_list(), self.probe_get_result_operation_system_list(), self.probe_get_result_total_node_count(), self.probe_get_result_location_list(), self.probe_get_result_server_ttl_list()

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
        start_time = timeit.default_timer()
        for current_ttl_value in range(1, _traceroute_max_ttl + 1):
            total_node_count = total_node_count + 1
            send_packet = IP(dst=_traceroute_target_protocol_address, ttl=current_ttl_value) / ICMP()
            response_packet = sr1(send_packet, verbose=_traceroute_verbose, timeout=_traceroute_timeout, iface=_traceroute_interface)

            if response_packet is not None: # arrive target
                if response_packet.type == 0:  # icmp echo reply
                    protocol_address_list.append(response_packet.getlayer(IP).src) # ip address
                    protocol_address = response_packet.getlayer(IP).src
                    operation_system, server_ttl = self.probe_operation_system(response_packet.getlayer(IP).ttl,
                                                                             total_node_count)
                    operation_system_list.append(operation_system) # operation system
                    server_ttl_list.append(server_ttl)
                    node_location = self.probe_check_location(str(protocol_address))
                    self.probe_print_result_step_by_step(str(protocol_address), str(operation_system),
                                                         str(node_location), str(server_ttl), str(total_node_count))
                    break
                else: # not target
                    protocol_address_list.append(response_packet.getlayer(IP).src) # ip address
                    protocol_address = response_packet.getlayer(IP).src
                    operation_system, server_ttl = self.probe_operation_system(response_packet.getlayer(IP).ttl,
                                                                             total_node_count)
                    operation_system_list.append(operation_system) # operation system
                    server_ttl_list.append(server_ttl)
                    node_location = self.probe_check_location(str(protocol_address))
            else: # not receive packet
                protocol_address = "Unknown"
                operation_system = "Unknown"
                server_ttl = "Unknown"
                protocol_address_list.append("Unknown")
                operation_system_list.append("Unknown")
                server_ttl_list.append("Unknown")
                node_location = self.probe_check_location(str(protocol_address))
            self.probe_print_result_step_by_step(str(protocol_address), str(operation_system), str(node_location),
                                                 str(server_ttl), str(total_node_count))
        end_time = timeit.default_timer()
        probe_time = end_time - start_time
        self.probe_print_result_overall(probe_time, total_node_count)
        return # total_node_count, protocol_address_list, operation_system_list, server_ttl_list, self.probe_node_location(total_node_count, protocol_address_list)

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
                    location_list.append("403 Error")
            else:
                location_list.append("Unknown")
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

    ## Renewal Zone : Print Result Step By Step ##

    """ @print result step by step function
    """
    def probe_print_result_step_by_step(self, _result_protocol_address, _result_operation_system, _result_location, _result_server_ttl, _result_node_number):
        result = " node " + str(_result_node_number) + ", IP : " + str(_result_protocol_address) + " / OS : " + str(_result_operation_system) + " / GEO : " + str(_result_location) + " / TTL : " + str(_result_server_ttl)
        print(result)
        return

    """ @check location geo
    @:param
        result protocol address : ip address
    @:return
        geo / unknown / 403
    """
    def probe_check_location(self, _result_protocol_address):
        is_ip_address = is_protocol_address(_result_protocol_address)
        result = ""
        if is_ip_address == 1:
            try:
                api_url = "http://www.geoplugin.net/json.gp?ip="
                url = api_url + str(_result_protocol_address)
                response = urlopen(url)
                data = json.load(response)
                location_string = str(data["geoplugin_countryName"])
                if location_string == "None":
                    result = "Unknown"
                else:
                    result = str(location_string)
            except: # ConnectionResetError
                result = "403 Error"
        else:
            result = "Unknown"
        return result

    def probe_print_result_overall(self, _probe_time, _total_node_count):
        result = "\n" \
                 " probe engine terminated (probe time : " + str(_probe_time) + " seconds)\n" \
                 " Total nodes : " + str(_total_node_count) + "\n"
        print(result)
        return

    """ @set-get zone
    @:set : traceroute_target_protocol_address
            traceroute_max_ttl
            traceroute_verbose
            traceroute_timeout
            traceroute_interface
    @:get : traceroute_target_protocol_address
            traceroute_max_ttl
            traceroute_verbose
            traceroute_timeout
            traceroute_interface
            result_total_node_count
            result_protocol_address_list
            result_location_list
            result_operation_system_list
            result_server_ttl_list
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