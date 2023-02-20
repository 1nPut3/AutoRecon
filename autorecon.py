# !/usr/bin/env python
"""
################################################################################

Welcome to AutoRecon
Created by 1nPut3

This is a simple scanning framework which allows the user to tag the most common
commands used for ctfs on HackTheBox, TryHackMe, Ext.

If You find a bug please put comment in the issues page @ the GitHub repository.

Anybody can copy and improve the code as long as you give credit where credit is due.

################################################################################
"""

from subprocess import call
from default_scan import default_scan
from quick_scan import quick_scan
from slow_scan import slow_scan
from intense_scan import intense_scan
from ghost_scan import ghost_scan
from banner import banner


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
        intense_scan()
    elif scan_type == "5":
        ghost_scan()
    elif scan_type == "6":
        print("[*] Starting Custom Scan...")
        print("[*] Scan complete!")
        print("[*] Going back to home screen...")

    elif scan_type == "99":
        print("[*] Exiting...")
        call(['clear', ])
        exit()

    else:
        print("please enter a valid choice!")
# ####END OF menu_choices################################################


def menu():
    while True:
        try:
            banner()
            print("________________________________________________")
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
            print("[4]: Intense Scan")
            print("")
            print("")
            print("[5]: Ghost Scan ( Warning Very slow!)")
            print("")
            print("")
            print("[6]: Default Scan + Enumeration(Not Done)")
            print("")
            print("")
            print("[99]: Exit")
            print("")
            scan_type = input("What scan do you want to run?: ")
            menu_choices(scan_type)

        except(KeyboardInterrupt):
            print("")
            print("")
            print("[*] KeyboardInterrupt detected. ")
            print("[*] Please type 99 to exit!")
            print("")


call(['clear', ])
menu()
