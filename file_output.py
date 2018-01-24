#!/usr/bin/env python


from subprocess import call
from get_ip import ip
def output(save_location, target):
    call(['touch', save_location + '/' + str(target) + '_scan.txt'])

    nmap_scan = open(save_location + "/nmap.txt", "r")
    nikto_scan = open(save_location + "/nikto.txt", "r")
    scan_results = nmap_scan.read() + nikto_scan.read()
    nikto_scan.close()
    nmap_scan.close()

    scan_result_data = open(save_location + '/' + str(target) + '_scan.txt','w')
    scan_result_data.write(scan_results)
    print("Saved Data to " + save_location)
    call(['sudo', 'rm', save_location + "/nikto.txt", save_location + "/nmap.txt"])
    scan_result_data.close()
