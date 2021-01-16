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
from scapy.layers.inet import traceroute, UDP, IP
from scapy.sendrecv import sr1

from src.package import cui

import collections

def main():
    # main_cui_engine = cui.Cui()
    # main_cui_engine.cui_engine()

    # result, unans = traceroute(["github.com"], maxttl = 20, verbose = 0)

    # result.show()
    # print(result.show())
    # result.summary()
    # r = result.show()
    # result.show()

    target = "52.78.231.108"
    max_ttl = 40
    destination_port = 32323
    verbose_value = 0
    timeout_value = 3

    for i in range(1, max_ttl):
        print(i, " count..")
        send_packet = IP(dst = target, ttl = i) / UDP(dport = destination_port)
        response_packet = sr1(send_packet, verbose = verbose_value, timeout = timeout_value)

        if response_packet is not None:
            if response_packet.type == 3:
                print("finish !! " + response_packet.getlayer(IP).src)
            else:
                print(response_packet.getlayer(IP).src)
        """
        if response_packet is None:
            break
        elif response_packet.type == 3:
            break
        else:
            print(i)
        """


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



