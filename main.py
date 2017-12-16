"""
################################################################################

Welcome to AutoRecon
Created by 1nPut3

This is still in development and will most likley have many bugs and spelling errors.

If You find a bug please put comment in the issues page @ the GitHub repository.

Anybody can copy and improve the code as long as you give credit where credit is due.

Many more imrovments are on the way like complete ghost scan, easy to read printed results
in one file from all a scan, a banner, more documentation, and more.
################################################################################
"""



#!/usr/bin/env python

from subprocess import call
from default_scan import default_scan


# Pick from the menu choices fuction
def menu_choices(scan_type):
    print("")
    if scan_type == "1":
        default_scan()
        menu()
    elif scan_type == "2":
        print("[*] Starting Fast Scan...")
        target = ip()
        website = is_website()
        print("[*] Scan complete!")
        print("[*] Going back to home screen...")

    elif scan_type == "3":
        print("[*] Starting Quiet Scan...")
        target = ip()
        website = is_website()
        print("[*] Scan complete!")
        print("[*] Going back to home screen...")

    elif scan_type == "4":
        print("[*] Starting Loud Scan...")
        target = ip()
        website = is_website()
        print("[*] Scan complete!")
        print("[*] Going back to home screen...")

    elif scan_type == "5":
        print("Warning this scan is very slow and will take a few days to scan!")
        warning = raw_input("Are you sure you want to continue?[y/n]: ")
        if warning == 'y':
            print("[*] Starting Ghost Scan...")
            print("[*] This will take a while")
            target = ip()
            website = is_website()
            print("[*] Scan complete!")
            print("[*] Going back to home screen...")
        elif warning =='n':
            print("[*] Going back to menu...")
            menu()
        else:
            print("[*] Sorry not an option going back to home screen.")
            menu()
    elif scan_type == "6":
        print("[*] Starting Custom Scan...")
        target = ip()
        website = is_website()
        print("[*] Scan complete!")
        print("[*] Going back to home screen...")

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
        print("[2]: Fast Scan")
        print("")
        print("")
        print("[3]: Quiet Scan")
        print("")
        print("")
        print("[4]: Loud Scan")
        print("")
        print("")
        print("[5]: Ghost Scan ( Warning Very slow! )")
        print("")
        print("")
        print("[6]: Custom Scan")
        print("")
        print("")
        print("[99]: Exit")
        scan_type = raw_input("What scan do you want to run?: ")
        menu_choices(scan_type)

    except(KeyboardInterrupt):
        print("[*] KeyboardInterrupt detected. ")
        print("[*] Exiting...")
        print("")

call(['clear',])
menu()
