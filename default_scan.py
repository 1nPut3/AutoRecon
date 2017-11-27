#!/usr/bin/env python
import subprocess
import nmap_scan, nikto_scan
def run(target,website):
    ###### Default scan protocol ######
    # Start nmap scan
    # If website start nikto scan
    # If website and using word press start wpscan

    print("[*] starting nmap scan...")
    nmap_scan.scan(target)
    if website == 'y':
        nikto_scan.scan(True,target)
    else:
        nikto_scan.scan(False, target)
    print("[*] Starting wpscan(NOT DONE)...")
