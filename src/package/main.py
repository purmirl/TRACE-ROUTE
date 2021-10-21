"""
 Copyright 2020~ PeTrA. All rights reserved.
 . Python Project Structure Repository;

 Probe Arrow Project (Advanced Trace Route) by PeTrA. 2020~
 ProbeArrow 1.0
 Language : Python3.8.2 on pycharm IDE
 Library : Scapy2.4.3
 API : IP Geo Location [geoplugin.net] --> http://www.geoplugin.net/json
 ------
 @ main.py
    * ProbeArrow/src/package/main.py
    * main function code file
"""

from src.package import cui

""" @main function
"""
def main():
    main_cui_engine = cui.Cui()
    main_cui_engine.cui_engine()
    return

""" @call main
"""
if __name__ == "__main__":
    main() # main function