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
from src.package import cui

""" main function
"""
def main():
    main_cui_engine = cui.Cui()
    main_cui_engine.cui_engine()


if __name__ == "__main__":
    main()




