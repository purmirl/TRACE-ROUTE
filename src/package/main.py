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
from pip._vendor import requests


def main():
    # main_cui_engine = cui.Cui()
    # main_cui_engine.cui_engine()

    url = "http://ip-api.com/json/"
    target = "121.121.121.121"
    headers = {
        "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
    }
    try:
        response = requests.get(url = url + target, headers = headers)

    except ConnectionResetError:
        pass

    json_response = response.json()
    print(json_response)



    # try:
    #     request = urllib.request.get(url + target)
    #     response = urllib.request.urlopen(request).read()
    #     json_response = json.loads(response.decode("utf-8"))
    #     print(json_response["country"])
    # except ConnectionResetError:
    #
    #     print("??")
    #     return

################################
    # header = {
    #     "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
    #     "Accept-Encoding": "*",
    #     "Connection": "keep-alive"
    # }
    # response = requests.get(url = url + target)
    #
    #
    # json_response = response.json().get("country")
    # print(json_response)
################################

    # user_agent = {"User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"}
    # try:
    #     request = urllib.request.get(url + target, headers = {"User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"})
    #     response = urllib.request.urlopen(request).read()
    #     json_response = json.loads(response.decode("utf-8"))
    #     print(json_response["country"])
    # except ConnectionResetError:
    #
    #     print("??")
    #     return
################################

    # traceroute parameter value

    """
    traceroute_target_protocol_address = "github.com"
    traceroute_max_ttl = 40
    traceroute_verbose = 0
    traceroute_timeout = 3

    probe_check = probe.Probe()
    probe_check.probe_traceroute(traceroute_target_protocol_address, traceroute_max_ttl,
                                 traceroute_verbose, traceroute_timeout)

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



