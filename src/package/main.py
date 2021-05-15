"""
 Copyright 2020~ PeTrA. All rights reserved.
 . Python Project Structure Repository;

 Probe Arrow Project by PeTrA. 2020
 ProbeArrow 1.0
 Language : Python3.8.2
 Library : Scapy2.4.3

 Advanced Trace Route
 ------
 Introduce of ProbeArrow
 ProbeArrow is Advanced Trace Route Program in Arrow Project.
 ------
 @ main.py
    * main function code file

"""

# ProbeArrow/src/main.py;
import requests
from scapy.layers.inet import IP, ICMP
from scapy.sendrecv import sr1

from src.package import cui

""" traceroute function
"""

def traceourte():
    # result, unans = traceroute(["github.com"], maxttl = 20, verbose = 0)

    # result.show()
    # print(result.show())
    # result.summary()
    # r = result.show()
    # result.show()

    target = "8.8.8.8"
    max_ttl = 40
    destination_port = 32323
    verbose_value = 0
    timeout_value = 3

    for i in range(1, max_ttl):
        print(i, " count..")
        # send_packet = IP(dst = target, ttl = i) / UDP(dport = destination_port)
        send_packet = IP(dst=target, ttl=i) / ICMP()
        response_packet = sr1(send_packet, verbose = verbose_value, timeout = timeout_value)

        if response_packet is not None:
            if response_packet.type == 0: # icmp echo reply
                print("finish !! " + response_packet.getlayer(IP).src)
                break
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


""" main function
"""
def main():
    # main_cui_engine = cui.Cui()
    # main_cui_engine.cui_engine()

    # traceourte()
    api_url = "https://ip-api.com/json/"
    protocol_address = "8.8.8.8"
    url = api_url + protocol_address
    print(url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}

    response = requests.get(url, headers = headers)
    print(response)

if __name__ == "__main__":
    main()




