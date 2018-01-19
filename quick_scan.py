#!/usr/bin/env python

from subprocess import call
from time import sleep
from file_output import output
from get_ip import ip
from is_website import is_website

def quick_scan():
    target = ip()
    print("")
    save_location = raw_input("Scan results save location?: ")
    web = is_website()
    print("[*] Starting Quick Scan...")
    call(['nmap' ,'-O' ,'-T4' ,'-sS' , str(target), '-oN', save_location + "/nmap.txt"])
    call(['nikto','-h', str(target),'-Plugins','@@ALL' ,'-o', save_location + "/nikto.txt"])
    print("[*] Saving scan Data...")
    output(save_location,web)
    print("[*] Going back to home screen...")
