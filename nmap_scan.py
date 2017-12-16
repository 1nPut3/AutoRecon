#!/usr/bin/env python


import subprocess

def nmap_scan(target, save_location):
    save = str(save_location)
    subprocess.call(['nmap','-sV','-O',str(target), '-oN', save + "/nmap.txt"])
