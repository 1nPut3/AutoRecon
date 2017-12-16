#!/usr/bin/env python
from subprocess import call
from nmap_scan import nmap_scan
from nikto_scan import nikto_scan
from time import sleep
from file_output import output
from get_ip import ip
from get_save import save_location
from is_website import is_website
from file_output import output
###### Default scan protocol ######
# Start nmap scan
# If website start nikto scan
# If website and using word press start wpscan

def default_scan():
    target = ip()
    print("")
    location = raw_input("Scan results save location?: ")
    web = is_website()
    print("[*] Starting Default Scan...")
    print("[*] starting nmap scan...")
    nmap_scan(target, location)
    nikto_scan(web,target, location)
    print("[*] Starting wpscan(NOT DONE)...")
    print("[*] Scan complete!")
    print("[*] Saving scan Data...")
    output(location)
    sleep(1)
    print("[*] Going back to home screen...")
    print(" ")
