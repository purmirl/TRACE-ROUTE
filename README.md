ProbeArrow
========================
**_ProbeArrow_ [Version 2102.01]** :: _The Advanced Trace Route_   
_Copyright 2020~ PeTrA. All rights reserved._   
## Preview
![06](https://user-images.githubusercontent.com/33143731/118299856-42d68980-b51c-11eb-833c-65e073f6af26.png)   
![07](https://user-images.githubusercontent.com/33143731/118300033-76b1af00-b51c-11eb-88de-19a2ba4d4451.png)
## Dev Environment
* _Language : Python3_   
* _OS : Microsoft Windows 10 64bits Operation_   
* _IDE : JetBrains Pycharm Series_   
* _Using Library : Python Scapy 2.4.3_   
* _Using API : ip-api.com/json/ (TCP/80 HTTP)_
## Explanation
The **_Probe Arrow_** is advanced trace route. The whole structure is **_@trace route module_** and **_@ip location module_**. Using python Scapy library for trace route, and Using ip-api json for ip location module. In trace route module, Using ICMP traceroute. (trace route : TCP trace route, UDP trace route, ICMP trace route, DNS trace route)   
## Trace Route Introduce
Trace route is thinking about the route by target ip. Trace route can take nodes (getting route or Layer (osi 7 layer) 3 equip) and ip address. That function is usually TCP, UDP, ICMP, DNS protocol for trace. For searching one nodes, one nodes to step, setting the TTL(Time To Live) header in IP header. First, set the TTL value to 1, arrive first node, TTL is change to 0, and first node reply the packet ICMP Time Exceeded.   
   
![05](https://user-images.githubusercontent.com/33143731/117476238-ead9d900-af97-11eb-913e-481c4a70990b.png)  
* **_TCP Trace Route_** : Using TCP(Transmission Control Protocol) for trace. Default setting is TTL in IP(Internet Protocol) header. Almost TCP Trace route is using TCP/80(HTTP), because almost target is web server, so that may be opening the port 80.   
* **_UDP Trace Route_** : Using UDP(User Datagram Protocol) for trace. Default setting is also TTL in IP(Internet Protocol) header. For example, using DNS(Domain Name System) trace is one of the UDP trace route (UDP/53).   
* **_ICMP Trace Route_** : Using ICMP(Internet Control Message Protocol) for trace. Default setting is also TTL in IP(Internet Protocol) header. In type of ICMP, Using type 128 (ICMP echo request).   
## IP Location Introduce
If we can ip address list by trace route module, need to find where is this ip address. That can use **_WHOIS_** service. **_WHOIS_** is a data structure that is query of ip address information and that's detailed information (location and management information). And, Whois is not a one area, but a string of many things.   
   
![02](https://user-images.githubusercontent.com/33143731/107150742-ae9bda00-69a2-11eb-9437-0b4756c05f5d.png)   
The Probe Arrow's IP Location module is used the database of IP address's information of API. That api is **_ip_api.com_**. This api is returne tha json data structure. This json structeure is it.   
   
![03](https://user-images.githubusercontent.com/33143731/107151607-cf662e80-69a6-11eb-89e9-7207aee422b6.png)   
So, the Porbe Arrow process result is IP List (Trace route module's result) and IP Location (IP Location module's result). Now look about structure of Probe Arrow Program. To sum up, First start traceroute function. The function is print that ip list of middle nodes as L3 layer's equip or routing protocol's boundary point. That results is the parameter of the ip location function that will print the result of the ip address's physical location. That is.   
   
@ _made by purmirl.petra 2020~_
