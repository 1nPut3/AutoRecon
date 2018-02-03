#!/usr/bin/env python

import os
from subprocess import call
from time import sleep
from file_output import output
from get_ip import ip

def ghost_scan():
    target = ip()
    call(['clear',])
    print("")

    #SAVE LOCATION
    user = os.path.expanduser('~')
    save_location = user +"/Documents"

    print("")
    print("[*] Starting Ghost Scan...")
    print("")

    call(['nmap', '-Pn', '-sT', '-T1', '-p', '80,443,21,22,23,25,53,110,135,137,139,1433,1434', str(target), '-oN', save_location + "/nmap.txt"])

    print("[*] Saving scan Data...")
    print("")
    
    output(save_location, target)
    print("[*] Going back to home screen...")
