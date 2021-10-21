"""
 Copyright 2020~ PeTrA. All rights reserved.
 . Python Project Structure Repository;

 Probe Arrow Project (Advanced Trace Route) by PeTrA. 2020~
 ProbeArrow 1.0
 Language : Python3.8.2 on pycharm IDE
 Library : Scapy2.4.3
 API : IP Geo Location [geoplugin.net] --> http://www.geoplugin.net/json
 ------
 @ cui.py
    * ProbeArrow/src/package/cui.py
    * console user interface code file
"""
import timeit
from scapy.arch import IFACES
from src.package import probe
from src.package.function import is_protocol_address

""" @Cui class
"""
class Cui:
    def __init__(self):
        return

    """ @cui engine function
    @:map
        @:main
            @:traceroute
                @:ip address
                @:quit
            @:show
                @:version
                @:quit
            @:exit
    """
    def cui_engine(self):
        self.print_rights()
        while True:
            HIVE_MAIN_COMMAND = self.get_command("main")
            if HIVE_MAIN_COMMAND == "?":
                self.print_main_option()
                continue
            elif HIVE_MAIN_COMMAND == "traceroute":
                self.print_move_comments("main", "traceroute")
                while True:
                    HIVE_TRACEROUTE_COMMAND = self.get_command("traceroute")
                    if HIVE_TRACEROUTE_COMMAND == "?":
                        self.print_traceroute_option()
                        continue
                    elif HIVE_TRACEROUTE_COMMAND == "":
                        continue
                    elif HIVE_TRACEROUTE_COMMAND == "quit":
                        self.print_move_comments("traceroute", "main")
                        break
                    else:  # something is put.
                        is_ip_address = is_protocol_address(HIVE_TRACEROUTE_COMMAND)
                        # print(is_ip_address)
                        if is_ip_address == 0:  # not ip address
                            self.print_ip_error()
                            continue
                        interface = self.config_set_interfaces()
                        self.run_traceroute(HIVE_TRACEROUTE_COMMAND, 40, 0, 3, interface)  # trace route engine start
                        continue
                    continue
                continue
            elif HIVE_MAIN_COMMAND == "show":
                self.print_move_comments("main", "show")
                while True:
                    HIVE_SHOW_COMMAND = self.get_command("show")
                    if HIVE_SHOW_COMMAND == "?":
                        self.print_show_option()
                        continue
                    elif HIVE_SHOW_COMMAND == "version":
                        # print software version
                        self.print_software_version()
                        continue
                    elif HIVE_SHOW_COMMAND == "quit":
                        self.print_move_comments("show", "main")
                        break
                    else:
                        continue
                    continue
                continue
            elif HIVE_MAIN_COMMAND == "exit":
                break
        return

    """ @cui print option zone
    """

    """ @main option
            traceroute
            show
            exit
    """
    def print_main_option(self):
        MAIN_OPTION = "\n" \
                      " 01. traceroute : start trace route \n" \
                      " 02. show : show program status \n" \
                      " 03. exit : program exit \n" \
                      ""
        print(MAIN_OPTION)
        return

    """ @show option
            version
    """
    def print_show_option(self):
        SHOW_OPTION = "\n" \
                      " 01. version : show software version \n" \
                      " 02. quit : quit show option \n" \
                      ""
        print(SHOW_OPTION)
        return

    """ @traceroute option
            [traget ip address]
    """
    def print_traceroute_option(self):
        TRACEROUTE_OPTION = "\n" \
                            " 01. [target ip address] : write target ip address for search \n" \
                            " 02. quit : quit traceroute option \n" \
                            ""
        print(TRACEROUTE_OPTION)
        return

    def print_ip_error(self):
        IP_ERROR_STRING = "\n" \
                          " This is not Internet Protocol address. \n" \
                          ""
        print(IP_ERROR_STRING)
        return

    def print_software_version(self):
        SOFTWARE_VERSION_STRING = "\n" \
                                  " ProbeArrow v 1.0 by PeTrA. 2021.JULY Updated.\n" \
                                  ""
        print(SOFTWARE_VERSION_STRING)
        return

    def print_rights(self):
        print("Copyright 2020~ PeTrA. All rights reserved.")
        print("ProbeArrow 1.0\n")
        return

    def print_move_comments(self, _from, _to):
        MOVE_COMMENTS_STRING = "\n" \
                               " move from " + str(_from) + " to " + str(_to) + "\n"
        print(MOVE_COMMENTS_STRING)
        return

    def get_command(self, _layer_name):
        result = ""
        result = input(_layer_name + "@probearrow:~# ")
        return result

    def parsing_interfaces_name(self, _string):
        _string = str(_string)
        key = 0
        interfaces = ""
        for i in range(0, len(_string)):
            if (_string[i] == "]"):
                key = 0
            if (key == 1):
                interfaces = interfaces + _string[i]
            if (_string[i] == "["):
               key = 1
        return interfaces

    def print_interfaces_list(self):
        interfaces_list = list((IFACES.data).values())
        for i in range(0, len(interfaces_list)):
            result = " " + str(i + 1) + ". " + str(self.parsing_interfaces_name(interfaces_list[i]))
            print(result)
        print()
        return

    def set_interfaces(self, _index):
        interfaces_list = list((IFACES.data).values())
        interfaces = ""
        for i in range(0, len(interfaces_list)):
            if(i == (_index - 1)):
                interfaces = self.parsing_interfaces_name(interfaces_list[i])
                break
        result = interfaces
        return result

    def config_set_interfaces(self):
        COMMENTS = "\n" \
                   " select internet interface ↓" \
                   "\n" \
                   ""
        print(COMMENTS)
        self.print_interfaces_list()
        index = ""
        index = input(" interface number : ")

        interfaces = self.set_interfaces(int(index))
        result = interfaces
        return result

    """ @cui traceroute engine zone
    """

    """ @run traceroute function
    @:param
        traceroute target protocol address
        traceroute max ttl
        traceroute verbose
        traceroute timeout
    """
    def run_traceroute(self, _traceroute_target_protocol_address, _traceroute_max_ttl,
                       _traceroute_verbose, _traceroute_timeout, _traceroute_interface):
        print()
        print(" traceroute operation proceeding...")
        print()
        start_time = timeit.default_timer()
        probe_traceroute_instance = probe.Probe()
        result_protocol_address_list, result_system_operation_list, result_total_node_count, result_node_location, result_server_ttl_list = \
            probe_traceroute_instance.probe_engine(_traceroute_target_protocol_address, _traceroute_max_ttl,
                                                   _traceroute_verbose, _traceroute_timeout, _traceroute_interface)
        return

""" @cui run traceroute function. backup - 20211021
    def run_traceroute(self, _traceroute_target_protocol_address, _traceroute_max_ttl,
                       _traceroute_verbose, _traceroute_timeout, _traceroute_interface):
        print()
        print(" traceroute operation proceeding...")
        print()
        start_time = timeit.default_timer()
        probe_traceroute_instance = probe.Probe()
        result_protocol_address_list, result_system_operation_list, result_total_node_count, result_node_location, result_server_ttl_list = \
            probe_traceroute_instance.probe_engine(_traceroute_target_protocol_address, _traceroute_max_ttl,
                                                   _traceroute_verbose, _traceroute_timeout, _traceroute_interface)
        result = "\n"
        for i in range(0, result_total_node_count):
            result = result + " node " + str(i + 1) + " : " + str(result_protocol_address_list[i]) + \
                     " ( OS : " + str(result_system_operation_list[i]) + " )" + " ( GEO : " + str(result_node_location[i]) + " )" + " ( TTL : " + str(result_server_ttl_list[i]) + " )\n"
        end_time = timeit.default_timer()
        result = result + "\n" + " probe engine terminated (probe time : " + str(end_time - start_time) + " seconds)\n" \
                                                                                                          " Total nodes : " + str(
            result_total_node_count) + "\n"
        # print(result)
        return
"""
""" @demo trace route function. back up - 20210516
    def run_traceroute_demo(self, _traceroute_target_protocol_address, _traceroute_max_ttl,
                            _traceroute_verbose, _traceroute_timeout):
        start_time = timeit.default_timer()
        probe_traceroute_instance = probe.Probe()
        result_protocol_address_list, result_system_operation_list, result_total_node_count = \
            probe_traceroute_instance.probe_demo(_traceroute_target_protocol_address, _traceroute_max_ttl,
                                                 _traceroute_verbose, _traceroute_timeout)
        result = "\n"
        for i in range(0, result_total_node_count):
            result = result + " node " + str(i + 1) + " : " + str(result_protocol_address_list[i]) + \
                     " ( " + str(result_system_operation_list[i]) + " )\n"
        end_time = timeit.default_timer()
        result = result + "\n" + " probe engine terminated (probe time : " + str(end_time - start_time) + " seconds)\n" \
                                                                                                          " Total nodes : " + str(
            result_total_node_count) + "\n"
        print(result)
        return
"""
