import io
from setuptools import setup, find_packages

install_requies = [
    "scapy==2.4.3"
]

setup(
    name                            = "ProbeArrow",
    version                         = "2.0",
    description                     = "Advanced Trace Route",
    author                          = "HeeGwon Cho",
    author_email                    = "prumirl.petra@gmail.com",
    url                             = "https://github.com/purmirl/ProbeArrow",
    long_description                = open("README.md").read(),
    long_description_content_type   = "text/markdown",
    license                         = "BSD-3-Clause",
    test_suite                      = "nose.collector",
    python_requires                 = ">=3.5",
    packeges                        = find_packages(exclude=["tests"])
)