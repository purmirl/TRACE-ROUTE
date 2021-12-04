"""
 Copyright 2020~ PeTrA. All rights reserved.
 . Python Project Structure Repository;

 Probe Arrow Project (Advanced Trace Route) by PeTrA. 2020~
 ProbeArrow - version 2021.12.01
  . base of Python3.8.2 on pycharm IDE, Scapy2.4.3
  . using API : IP Geo Location [geoplugin.net] --> http://www.geoplugin.net/json
  . package is here --> https://github.com/purmirl/ProbeArrow

 @ function.py
    * ProbeArrow/src/package/function.py
    * utility function code file
"""

""" @parseProtocolAddress function
        parse protocol address (ip address)
        :parameter
            _protocolAddress : ip address
        :return
            Integer list [a, b, c, d]
"""
def parse_protocol_address(_protocol_address):
    length = len(_protocol_address)
    a = ""
    b = ""
    c = ""
    d = ""

    # return value : Integer a, b, c, d
    for i in range(0, length):
        if _protocol_address[i] == '.':
            flags = i
            break
        a = a + _protocol_address[i]

    for i in range(flags + 1, length):
        if _protocol_address[i] == '.':
            flags = i
            break
        b = b + _protocol_address[i]

    for i in range(flags + 1, length):
        if _protocol_address[i] == '.':
            flags = i
            break
        c = c + _protocol_address[i]

    for i in range(flags + 1, length):
        d = d + _protocol_address[i]

    result = [a, b, c, d]
    return result


""" @isProtocolAddress function
        check that is protocol address (ip address)
        :parameter
            _protocolAddress : ip address
        :return
            if protocol address : return 1
            else : return 0
"""
def is_protocol_address(_protocol_address):
    result = 1  # if protocol address : 1,   else : 0
    length = len(_protocol_address)
    protocol_address_data = ['.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    # check length
    # example : 127.0.0.1.2.3.4214214123123
    if length < 7 | length > 15:
        result = 0
        return result

    # check another character
    # example : 127.0:0.1
    for i in range(0, length):
        if _protocol_address[i] not in protocol_address_data:
            result = 0
            return result

    # check dot position
    # example : .127.0.0.1
    if _protocol_address[0] == '.':
        result = 0
        return result
    elif _protocol_address[length - 1] == '.':
        result = 0
        return result

    # check dot count
    # example : 127.0.0....1
    dot_count = 0
    for i in range(1, length + 1):
        if _protocol_address[i - 1] == '.':
            dot_count += 1
    if dot_count != 3:
        result = 0
        return result

    # print("dot count " + str(dot_count))

    # check continued dot
    # example : 127..0.0.1
    is_pre_dot = 0
    for i in range(0, length):
        if _protocol_address[i] == '.':
            if is_pre_dot == 1:
                result = 0
                return result
            else:
                is_pre_dot = 1
        else:
            is_pre_dot = 0

    # check 0 started number
    # example : 127.0.0.01
    parse_result = parse_protocol_address(_protocol_address)
    if (len(parse_result[0]) > 1) & (parse_result[0][0] == '0'):
        result = 0
        return result
    elif (len(parse_result[1]) > 1) & (parse_result[1][0] == '0'):
        result = 0
        return result
    elif (len(parse_result[2]) > 1) & (parse_result[2][0] == '0'):
        result = 0
        return result
    elif (len(parse_result[3]) > 1) & (parse_result[3][0] == '0'):
        result = 0
        return result

    # check number range
    # example : 256.255.255.255
    if (int(parse_result[0]) < 0) | (int(parse_result[0]) > 255):
        result = 0
        return result
    elif (int(parse_result[1]) < 0) | (int(parse_result[1]) > 255):
        result = 0
        return result
    elif (int(parse_result[2]) < 0) | (int(parse_result[2]) > 255):
        result = 0
        return result
    elif (int(parse_result[3]) < 0) | (int(parse_result[3]) > 255):
        result = 0
        return result
    return result