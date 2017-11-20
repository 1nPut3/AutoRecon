#!/usr/bin/env python


import subprocess, sys, time

def ip():
    print("")
    address = raw_input("Type in the targets ip address: ")
    return(address)

def menu_choices(scan_type):
    print("")
    if scan_type == "1":
        print("[*] Starting Default Scan...")
        target = ip()
    elif scan_type == "2":
        print("[*] Starting Light Scan...")
        target = ip()
    elif scan_type == "3":
        print("[*] Starting Fast Scan...")
        target = ip()
    elif scan_type == "4":
        print("[*] Starting Loud Scan...")
        target = ip()
    elif scan_type == "5":
        print("[*] Starting Custom Scan...")
        target = ip()
    elif scan_type == "99":
        print("[*] Exiting...")
        exit()
    else:
        print("please enter a valid choice!")

def menu():
    try:
        subprocess.call(['clear',])
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
        print("")
        print("[*] KeyboardInterrupt detected. ")
        print("[*] Exiting...")
        print("")
menu()
