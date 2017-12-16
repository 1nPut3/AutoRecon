#!/usr/bin/env python


from subprocess import call

def output(save_location):
    call(['touch', save_location + '/complete_scan.txt'])
    #save = input("Save result location: ")
    #call(['touch', save_location() + /, ])
    nmap_scan = open(save_location + "/nmap.txt", "r")
    nikto_scan = open(save_location + "/nikto.txt", "r")
    #spacer = open("scan_results/spacer.txt")

    #nmap_scan_data = nmap_scan_results.read()
    #nikto_scan_data = nikto_scan_results.read()
    #spacer_data = spacer.read()

    scan_results = nmap_scan.read() + nikto_scan.read()

    nmap_scan.close()
    nikto_scan.close()
    #spacer.close()

    scan_result_data = open(save_location + '/complete_scan.txt','w')
    scan_result_data.write(scan_results)

    scan_result_data.close()
