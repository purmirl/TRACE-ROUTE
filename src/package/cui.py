"""
 ProbeArrow
 Copyright 2020~ PeTrA. All rights reserved.
 . Python Project Structure Repository;

 Probe Arrow Project by PeTrA. 2020~
 ProbeArrow 1.0
 Language : Python3.8.2
 Library : Scapy2.4.3

 Advanced Trace Route
 ------
 @ cui.py
    * character user interface python code file
"""
import timeit

from src.package import probe
from src.package.function import is_protocol_address

class Cui():
    def __init__(self):
        return

    def cui_engine(self):
        self.print_rights()

        while True:
            HIVE_MAIN_COMMAND = self.get_command("main")
            if HIVE_MAIN_COMMAND == "?":
                self.print_main_option()
                continue
            elif HIVE_MAIN_COMMAND == "traceroute":
                while True:
                    HIVE_TRACEROUTE_COMMAND = self.get_command("traceroute")
                    if HIVE_TRACEROUTE_COMMAND == "?":
                        self.print_traceroute_option()
                        continue
                    elif HIVE_TRACEROUTE_COMMAND == "":
                        continue
                    elif HIVE_TRACEROUTE_COMMAND == "quit":
                        break
                    else: # something is put.
                        is_ip_address = is_protocol_address(HIVE_TRACEROUTE_COMMAND)
                        if is_ip_address == 0: # not ip address
                            self.print_ip_error()
                            continue
                        self.run_traceroute(HIVE_TRACEROUTE_COMMAND, 40, 0, 3) # trace route engine start
                        continue
                    continue
                continue
            elif HIVE_MAIN_COMMAND == "show":
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
                        break
                    else:
                        continue
                    continue
                continue
            elif HIVE_MAIN_COMMAND == "exit":
                break

    """ cui print option zone
    
    """
    """ main option
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

    """ show option
            version
    """
    def print_show_option(self):
        SHOW_OPTION = "\n" \
                      " 01. version : show software version \n" \
                      " 02. quit : quit show option \n" \
                      ""
        print(SHOW_OPTION)
        return

    """ traceroute option
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
                          " This is not Internet Protocol address. \n"\
                          ""
        print(IP_ERROR_STRING)
        return

    def print_software_version(self):
        SOFTWARE_VERSION_STRING = "\n" \
                                  " ProbeArrow v 1.0 by PeTrA. 2021.JAN Updated.\n" \
                                  ""
        print(SOFTWARE_VERSION_STRING)
        return

    def print_rights(self):
        print("Copyright 2020~ PeTrA. All rights reserved.")
        print("ProbeArrow 1.0\n")
        return

    def get_command(self, _layer_name):
        result = ""
        result = input(_layer_name + "@probearrow:~# ")
        return result

    """ cui traceroute engine zone
    
    """
    """ run traceroute function
    @:param
        traceroute target protocol address
        traceroute max ttl
        traceroute verbose
        traceroute timeout
    """
    def run_traceroute(self, _traceroute_target_protocol_address, _traceroute_max_ttl,
                         _traceroute_verbose, _traceroute_timeout):
        start_time = timeit.default_timer()
        probe_traceroute_instance = probe.Probe()
        result_protocol_address_list, result_location_list, result_total_node_count = \
            probe_traceroute_instance.probe_engine(_traceroute_target_protocol_address, _traceroute_max_ttl,
                         _traceroute_verbose, _traceroute_timeout)

        for i in range(0, result_total_node_count):
            result = ""
            result = " Total nodes : " + str(result_total_node_count) + "\n" \
                                                                      "\n" \
                     " node " + str(i) + " : " + str(result_protocol_address_list[i]) + \
                     " ( " + str(result_location_list[i]) + " )\n" \
                                                            "\n" \
                                                            ""
        end_time = timeit.default_timer()
        result = result + " probe engine terminated (probe time : " + str(end_time - start_time) + " seconds\n" \
                                                                                                   "\n" \
                                                                                                   ""
        print(result)

        return
