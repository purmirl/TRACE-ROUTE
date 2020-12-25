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

class Cui():

    def __init__(self):
        return

    def cui_engine(self):
        self.print_rights()

        while True:
            HIVE_MAIN_COMMAND = self.get_command("main")
            if HIVE_MAIN_COMMAND == "?":
                self.print_main_option()


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

    def print_rights(self):
        print("Copyright 2020~ PeTrA. All rights reserved.")
        print("ProbeArrow 1.0\n")
        return

    def get_command(self, _layer_name):
        result = ""
        result = input(_layer_name + "@probearrow:~# ")

        return result