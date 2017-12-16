#!/usr/bin/env python


from subprocess import call
def nikto_scan(web,target, save):
    if web == 'y':
        print("[*] Starting nikto scan...")
        call(['nikto', '-h', str(target) ,'-o', save + "/nikto.txt",])
    elif web == 'n':
        print("[*] Detected not webpage...")
        print("[*] Skipping nikto scan")
    else:
        # If error then abort task
        print("[*] Error aborting...")
