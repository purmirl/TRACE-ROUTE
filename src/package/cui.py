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
                        if is_ip_address == 0:
                            self.print_ip_error()
                            continue
                        ###########################################################################
                        # here, traceroute function is needed.
                        ###########################################################################
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
                        continue
                    elif HIVE_SHOW_COMMAND == "quit":
                        break
                    else:
                        continue
                    continue
                continue
            elif HIVE_MAIN_COMMAND == "exit":
                break




    # option line
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

    def print_rights(self):
        print("Copyright 2020~ PeTrA. All rights reserved.")
        print("ProbeArrow 1.0\n")
        return

    def get_command(self, _layer_name):
        result = ""
        result = input(_layer_name + "@probearrow:~# ")

        return result