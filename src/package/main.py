"""
 Copyright 2020~ PeTrA. All rights reserved.
 . Python Project Structure Repository;

 Probe Arrow Project by PeTrA. 2020
 ProbeArrow 1.0
 Language : Python3.8.2
 Library : Scapy2.4.3

 Advanced Trace Route
 ------
 @ main.py
    * main function code file
"""

# ProbeArrow/src/main.py;
from scapy.layers.inet import traceroute

from src.package import cui

import collections

def main():
    # main_cui_engine = cui.Cui()
    # main_cui_engine.cui_engine()

    result, unans = traceroute(["github.com"], maxttl = 20, verbose = 0)

    result.show()
    # result.show()
    return

"""
    my_list = collections.deque()

    my_list.append("127.0.0.1")
    print(my_list)
    print(my_list[0])
    my_list.append("8.8.8.8")
    print(my_list)
    print(my_list[0])

    print(my_list[1])
    print(len(my_list))
"""

if __name__ == "__main__":
    main()



