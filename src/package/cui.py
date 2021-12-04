"""
 Copyright 2020~ PeTrA. All rights reserved.
 . Python Project Structure Repository;

 Probe Arrow Project (Advanced Trace Route) by PeTrA. 2020~
 ProbeArrow - version 2021.12.01
  . base of Python3.8.2 on pycharm IDE, Scapy2.4.3
  . using API : IP Geo Location [geoplugin.net] --> http://www.geoplugin.net/json
  . package is here --> https://github.com/purmirl/ProbeArrow

 @ cui.py
    * ProbeArrow/src/package/cui.py
    * console user interface code file
"""

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
            cui_main_command = self.get_command("main")
            if cui_main_command == "?":
                self.print_main_option()
                continue
            elif cui_main_command == "traceroute":
                self.print_move_comments("main", "traceroute")
                while True:
                    cui_traceroute_command = self.get_command("traceroute")
                    if cui_traceroute_command == "?":
                        self.print_traceroute_option()
                        continue
                    elif cui_traceroute_command == "":
                        continue
                    elif cui_traceroute_command == "quit":
                        self.print_move_comments("traceroute", "main")
                        break
                    else:  # something is put.
                        is_ip_address = is_protocol_address(cui_traceroute_command)
                        # print(is_ip_address)
                        if is_ip_address == 0:  # not ip address
                            self.print_ip_error()
                            continue
                        interface = self.config_set_interfaces()
                        self.run_traceroute(cui_traceroute_command, 30, 0, 3, interface)  # trace route engine start
                        continue
                    continue
                continue
            elif cui_main_command == "show":
                self.print_move_comments("main", "show")
                while True:
                    cui_show_command = self.get_command("show")
                    if cui_show_command == "?":
                        self.print_show_option()
                        continue
                    elif cui_show_command == "version":
                        # print software version
                        self.print_software_version()
                        continue
                    elif cui_show_command == "quit":
                        self.print_move_comments("show", "main")
                        break
                    else:
                        continue
                    continue
                continue
            elif cui_main_command == "exit":
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
        main_option = "\n" \
                      " 01. traceroute : start trace route \n" \
                      " 02. show : show program status \n" \
                      " 03. exit : program exit \n" \
                      ""
        print(main_option)
        return

    """ @show option
            version
    """
    def print_show_option(self):
        show_option = "\n" \
                      " 01. version : show software version \n" \
                      " 02. quit : quit show option \n" \
                      ""
        print(show_option)
        return

    """ @traceroute option
            [traget ip address]
    """
    def print_traceroute_option(self):
        traceroute_option = "\n" \
                            " 01. [target ip address] : write target ip address for search \n" \
                            " 02. quit : quit traceroute option \n" \
                            ""
        print(traceroute_option)
        return

    """ @print ip error
    """
    def print_ip_error(self):
        ip_error_string = "\n" \
                          " This is not Internet Protocol address. \n" \
                          ""
        print(ip_error_string)
        return

    """ @print software version
    """
    def print_software_version(self):
        software_version_string = "\n" \
                                  " ProbeArrow v 2021.12.01 by PeTrA. 2021.DECEMBER Updated.\n" \
                                  ""
        print(software_version_string)
        return

    """ @print rights
    """
    def print_rights(self):
        print("Copyright 2020~ PeTrA. All rights reserved.")
        print("ProbeArrow 1.0\n")
        return

    """ print move comments
    """
    def print_move_comments(self, _from, _to):
        move_comments_string = "\n" \
                               " move from " + str(_from) + " to " + str(_to) + "\n"
        print(move_comments_string)
        return

    """ get command
    """
    def get_command(self, _layer_name):
        result = ""
        result = input(_layer_name + "@probearrow:~# ")
        return result

    """ @parsing interfaces name
    """
    def parsing_interfaces_name(self, _string):
        _string = str(_string)
        key = 0
        key_key = 0
        interfaces = ""
        for i in range(0, len(_string)):
            if (_string[i] == "]"):
                if (key == 1) and (key_key == 1):
                    key_key = 0
                else:
                    key = 0
            if (key == 1):
                interfaces = interfaces + _string[i]
            if (_string[i] == "["):
                if (key == 1):
                    key_key = 1
                else:
                    key = 1
        return interfaces

    """ @print interfaces list
    """
    def print_interfaces_list(self):
        interfaces_list = list((IFACES.data).values())
        for i in range(0, len(interfaces_list)):
            result = " " + str(i + 1) + ". " + str(self.parsing_interfaces_name(interfaces_list[i]))
            print(result)
        print()
        return

    """ @set interfaces
    """
    def set_interfaces(self, _index):
        interfaces_list = list((IFACES.data).values())
        interfaces = ""
        for i in range(0, len(interfaces_list)):
            if(i == (_index - 1)):
                interfaces = self.parsing_interfaces_name(interfaces_list[i])
                break
        result = interfaces
        return result

    """ @config set interfaces
    """
    def config_set_interfaces(self):
        comments = "\n" \
                   " select internet interface ↓" \
                   "\n" \
                   ""
        print(comments)
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
        probe_traceroute_instance = probe.Probe()
        probe_traceroute_instance.probe_engine(_traceroute_target_protocol_address, _traceroute_max_ttl,
                                                   _traceroute_verbose, _traceroute_timeout, _traceroute_interface)
        return
