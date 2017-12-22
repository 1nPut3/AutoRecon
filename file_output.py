#!/usr/bin/env python


from subprocess import call

def output(save_location , is_website):
    call(['touch', save_location + '/complete_scan.txt'])

    nmap_scan = open(save_location + "/nmap.txt", "r")
    if is_website == 'y':
        nikto_scan = open(save_location + "/nikto.txt", "r")
        scan_results = nmap_scan.read() + nikto_scan.read()
        nikto_scan.close()
    else:
        scan_results = nmap_scan.read()

    nmap_scan.close()

    scan_result_data = open(save_location + '/complete_scan.txt','w')
    scan_result_data.write(scan_results)

    scan_result_data.close()
