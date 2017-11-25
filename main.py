#!/usr/bin/env python


import subprocess, sys, time


# starts nikto scan if website and not silent scan
def nikto_scan(argument,target):
    if argument == True:
        print("[*] Starting nikto scan...")
        subprocess.call(['nikto', '-h', target ,'-o', '/root/Documents/results.txt',])
        return(1)
    elif argument == False:
        print("[*] Detected not webpage...")
        print("[*] Skipping nikto scan")
        return(1)
    else:
        # If error then abort task
        print("[*] Error aborting...")
        return(0)

def default_scan(target,website):
    ###### Default scan protocol ######
    # Start nmap scan
    # If website start nikto scan
    # If website and using word press start wpscan

    print("[*] starting nmap scan(not done yet)...")
    if website == 'y':
        nikto_scan(True,target)
    else:
        nikto_scan(False, target)
    print("[*] Starting wpscan...")
    menu()


# Ip address input function
def ip():
    print("")
    address = raw_input("Type in the targets ip address: ")
    return(address)


# If website function
def is_website():
    print("")
    website = raw_input("Is this ip address a website?[y/n]: ")
    return(website)

# Pick from the menu choices fuction
def menu_choices(scan_type):
    print("")
    if scan_type == "1":
        print("[*] Starting Default Scan...")
        target = ip()
        website = is_website()
        default_scan(target,website)
    elif scan_type == "2":
        print("[*] Starting Light Scan...")
        target = ip()
        website = is_website()
    elif scan_type == "3":
        print("[*] Starting Fast Scan...")
        target = ip()
        website = is_website()
    elif scan_type == "4":
        print("[*] Starting Loud Scan...")
        target = ip()
        website = is_website()
    elif scan_type == "5":
        print("[*] Starting Custom Scan...")
        target = ip()
        website = is_website()
    elif scan_type == "99":
        print("[*] Exiting...")
        exit()
    else:
        print("please enter a valid choice!")

def menu():
    try:
        print("________________________Main Menu____________________________")
        print("")
        print("")
        print("[1]: Default Scan")
        print("")
        print("")
        print("[2]: Light Scan")
        print("")
        print("")
        print("[3]: Fast Scan")
        print("")
        print("")
        print("[4]: Loud Scan")
        print("")
        print("")
        print("[5]: Custom Scan")
        print("")
        print("")
        print("[99]: Exit")
        scan_type = raw_input("What scan do you want to run?: ")
        menu_choices(scan_type)

    except(KeyboardInterrupt):
        print("[*] KeyboardInterrupt detected. ")
        print("[*] Exiting...")
        print("")
subprocess.call(['clear',])
menu()
