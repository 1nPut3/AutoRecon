#!/usr/bin/env python


import subprocess, sys, time

def menu():
    subprocess.call(['clear',])
    print("________________________Main Menu____________________________")
    print("")
    print("")
    print("[1] Default Scan")
    print("")
    print("")
    print("[2] Light Scan")
    print("")
    print("")
    print("[3] Fast Scan")
    print("")
    print("")
    print("[4] Loud Scan")
    print("")
    print("")
    print("[5] Custom Scan")
    print("")
    print("")
    scan_type = raw_input("What scan do you whant to preform?: ")
    

menu()
