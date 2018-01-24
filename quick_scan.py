#!/usr/bin/env python
import os
from subprocess import call
from time import sleep
from file_output import output
from get_ip import ip
from is_website import is_website

def quick_scan():
    target = ip()
    call(['clear',])
    print("")
    user = os.path.expanduser('~')
    save_location = user +"/Documents"
    print("")
    # save_location = raw_input("Scan results save location?: ")
    print("[*] Starting Quick Scan...")
    print("")
    call(['nmap' ,'-O' ,'-T4' ,'-sS' , str(target), '-oN', save_location + "/nmap.txt"])
    call(['nikto','-h', str(target),'-Plugins','@@ALL' ,'-o', save_location + "/nikto.txt"])
    print("[*] Saving scan Data...")
    print("")
    output(save_location, target)
    print("[*] Going back to home screen...")
