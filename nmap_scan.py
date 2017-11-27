#!/usr/bin/env python


import subprocess


def scan(target):
    subprocess.call(['nmap','-sV','-O',target, '-oN', '/root/Documents/nmap_scan.txt'])
