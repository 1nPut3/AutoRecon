"""
################################################################################

Welcome to AutoRecon
Created by 1nPut3

This is still in development and will most likley have many bugs and spelling errors.

If You find a bug please put comment in the issues page @ the GitHub repository.

Anybody can copy and improve the code as long as you give credit where credit is due.

Many more imrovments are on the way like complete ghost scan, easy to read printed results
in one file from all scanners, a banner, more documentation, and more.
################################################################################
"""



#!/usr/bin/env python

from subprocess import call
from default_scan import default_scan
from quick_scan import quick_scan
from time import sleep
from slow_scan import slow_scan

# Pick from the menu choices fuction
def menu_choices(scan_type):
    print("")
    if scan_type == "1":
        default_scan()
    elif scan_type == "2":
        quick_scan()
    elif scan_type == "3":
        slow_scan()
    elif scan_type == "4":
        print("[*] Starting Intense/Loud Scan...")

        print("[*] Scan complete!")
        print("[*] Going back to home screen...")

    elif scan_type == "5":
        print("Warning this scan is very slow and will take a few days to scan!")
        warning = raw_input("Are you sure you want to continue?[y/n]: ")
        if warning == 'y':
            print("[*] Starting Ghost Scan...")
            print("[*] This will take a while")
            print("[*] Scan complete!")
            print("[*] Going back to home screen...")
        elif warning =='n':
            print("[*] Going back to home screen...")
        else:
            print("[*] Sorry not an option going back to home screen...")
    elif scan_type == "6":
        print("[*] Starting Custom Scan...")
        print("[*] Scan complete!")
        print("[*] Going back to home screen...")

    elif scan_type == "99":
        print("[*] Exiting...")
        sleep(1)
        call(['clear',])
        exit()

    else:
        print("please enter a valid choice!")


def menu():
    while True:
        try:
            print("________________________Main Menu____________________________")
            print("")
            print("")
            print("[1]: Default Scan")
            print("")
            print("")
            print("[2]: Quick Scan")
            print("")
            print("")
            print("[3]: Slow Comprehensive Scan")
            print("")
            print("")
            print("[4]: Intense/Loud Scan(Not Done)")
            print("")
            print("")
            print("[5]: Ghost Scan ( Warning Very slow!(Not Done) )")
            print("")
            print("")
            print("[6]: Custom Scan(Not Done)")
            print("")
            print("")
            print("[99]: Exit")
            print("")
            scan_type = raw_input("What scan do you want to run?: ")
            menu_choices(scan_type)

        except(KeyboardInterrupt):
            print("")
            print("")
            print("[*] KeyboardInterrupt detected. ")
            print("[*] Please type 99 to exit!")
            print("")

call(['clear',])
menu()
