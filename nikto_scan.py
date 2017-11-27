#!/usr/bin/env python


import subprocess


def scan(argument,target):
    if argument == True:
        print("[*] Starting nikto scan...")
        subprocess.call(['nikto', '-h', target ,'-o', '/root/Documents/results.txt',])
    elif argument == False:
        print("[*] Detected not webpage...")
        print("[*] Skipping nikto scan")
    else:
        # If error then abort task
        print("[*] Error aborting...")
