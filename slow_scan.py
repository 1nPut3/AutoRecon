#!/usr/bin/env python

import os
from subprocess import call
from time import sleep
from file_output import output
from get_ip import ip

def slow_scan():
    target = ip()
    call(['clear',])
    print("")
    user = os.path.expanduser('~')
    save_location = user +"/Documents"
    print("")
    print("[*] Starting Slow/Comprehensive Scan...")
    print("")
    call(['nmap', '-sS', '-sU', '-T4', '-A', '-v', '-PE', '-PP', '-PS80,443', '-PA3389', '-PU40125', '-PY', '-g 53', '--script', "default or (discovery and safe)", str(target), '-oN', save_location + "/nmap.txt"])
    call(['nikto','-h', str(target),'-Plugins','@@ALL' ,'-o', save_location + "/nikto.txt"])
    print("[*] Saving scan Data...")
    print("")
    output(save_location, target)
    print("[*] Going back to home screen...")
