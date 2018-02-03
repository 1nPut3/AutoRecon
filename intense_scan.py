#!/usr/bin/env python


import os
from subprocess import call
from time import sleep
from file_output import output
from get_ip import ip

def intense_scan():
    target = ip()
    call(['clear',])
    print("")

    #SAVE LOCATION
    user = os.path.expanduser('~')
    save_location = user +"/Documents"

    print("")
    print("[*] Intense Scan...")
    print("")

    call(['nmap', '-sS', '-sU', '-T4', '-A', '-v', str(target), '-oN', save_location + "/nmap.txt"])
    call(['nikto','-h', str(target),'-Plugins','@@ALL' ,'-o', save_location + "/nikto.txt"])

    print("[*] Saving scan Data...")
    print("")
    
    output(save_location, target)
    print("[*] Going back to home screen...")
