#!/usr/bin/env python
from subprocess import call
import os
from time import sleep
from file_output import output
from get_ip import ip
from is_website import is_website

###### Default scan protocol ######
# Start nmap scan
# If website start nikto scan
# If website and using word press start wpscan

def default_scan():
    target = ip()
    print("")
    user = os.path.expanduser('~')
    save_location = user +"/Documents"
    call(['clear',])
    print("")
    # save_location = raw_input("Scan results save location?: ")
    print("[*] Starting Default Scan...")
    print("")
    print("[*] starting nmap scan...")
    print("")
    call(['nmap','-sV','-O',str(target), '-oN', save_location + "/nmap.txt"])
    call(['nikto','-h', str(target), '-o', save_location + "/nikto.txt"])
    print("[*] Scan complete!")
    print("")
    print("[*] Saving scan Data...")
    print("")
    output(save_location, target)
    sleep(1)
    print("[*] Going back to home screen...")
    print(" ")
