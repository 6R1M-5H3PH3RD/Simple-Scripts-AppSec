# The script begins by importing the subprocess and os modules, which are used to run external commands and interact with the operating system, respectively.
# The check_and_install_tool function takes a tool name as an argument and checks if the tool is installed. If it is not installed, it installs the tool using the pip package manager.
# The run_information_gathering_tools function runs several tools for information gathering, including dig, dnsenum, sublist3r, dnstracer, dnsrecon, nikto, and sslstrip.
# The run_scanning_and_enumeration_tools function runs several tools for scanning and enumeration, including nmap, dnsenum, openvas, enum4linux, sqlninja, dirb, and dnsdumpster.
# The run_exploitation_and_techniques_tools function runs several tools for exploitation and techniques, including sqlmap, veil-evasion, luckystrike, and hydra.
# The run_post_exploitation_tools function runs several tools for post-exploitation, including cobaltstrike, sherlock, mimikatz, and psattack.
# The script ends with a call to the run_all_tools function, which runs all of the above functions in sequence.

import subprocess
import os

def check_and_install_tool(tool_name):
  # Check if the tool is installed
  try:
    subprocess.run([tool_name, "--help"], check=True)
  except:
    # Tool is not installed, so install it
    print(f"Installing {tool_name}...")
    subprocess.run(["pip", "install", tool_name])

def run_information_gathering_tools():
  check_and_install_tool("dig")
  check_and_install_tool("dnsenum")
  check_and_install_tool("sublist3r")
  check_and_install_tool("dnstracer")
  check_and_install_tool("dnsrecon")
  check_and_install_tool("nikto")
  check_and_install_tool("sslstrip")

  # Run dig
  subprocess.run(["dig", "target_machine"])
  # Run dnsenum
  subprocess.run(["dnsenum", "target_machine"])
  # Run sublist3r
  subprocess.run(["sublist3r", "-d", "target_machine"])
  # Run dnstracer
  subprocess.run(["dnstracer", "target_machine"])
  # Run dnsrecon
  subprocess.run(["dnsrecon", "-d", "target_machine"])
  # Run nikto
  subprocess.run(["nikto", "-h", "target_machine"])
  # Run sslstrip
  subprocess.run(["sslstrip", "-l", "10000", "-w", "results.log"])

def run_scanning_and_enumeration_tools():
  check_and_install_tool("nmap")
  check_and_install_tool("dnsenum")
  check_and_install_tool("openvas")
  check_and_install_tool("enum4linux")
  check_and_install_tool("sqlninja")
  check_and_install_tool("dirb")
  check_and_install_tool("dnsdumpster")

  # Run nmap
  subprocess.run(["nmap", "-sV", "target_machine"])
  # Run dnsenum
  subprocess.run(["dnsenum", "target_machine"])
  # Run openvas
  subprocess.run(["openvas", "--host=target_machine"])
  # Run enum4linux
  subprocess.run(["enum4linux", "target_machine"])
  # Run sqlninja
  subprocess.run(["sqlninja", "-t", "target_machine"])
  # Run dirb
  subprocess.run(["dirb", "http://target_machine"])
  # Run dnsdumpster
  subprocess.run(["dnsdumpster", "-d", "target_machine"])

def run_exploitation_and_techniques_tools():
  check_and_install_tool("sqlmap")
  check_and_install_tool("veil-evasion")
  check_and_install_tool("luckystrike")
  check_and_install_tool("hydra")

#Run sqlmap
subprocess.run(["sqlmap", "-u", "http://target_machine/login"])

#Run veil-evasion
subprocess.run(["veil-evasion"])

#Run luckystrike
subprocess.run(["luckystrike"])

#Run hydra
subprocess.run(["hydra", "-l", "user", "-P", "password_list.txt", "target_machine", "ssh"])

def run_post_exploitation_tools():
	check_and_install_tool("cobaltstrike")
	check_and_install_tool("sherlock")
	check_and_install_tool("mimikatz")
	check_and_install_tool("psattack")

#Run cobalt strike
subprocess.run(["cobaltstrike"])

#Run sherlock
subprocess.run(["sherlock", "user"])

#Run mimikatz
subprocess.run(["mimikatz"])

#Run psattack
subprocess.run(["psattack"])

def generate_report():

#Use google hacking report template and generate the report using the output of all 1 to 4 steps
pass

def main():
	print("Select an option:")
	print("1. Information gathering")
	print("2. Scanning and Enumeration")
	print("3. Exploitation and techniques")
	print("4. Post-exploitation")
	print("5. Report generation")

option = input()

if option == "1":
	run_information_gathering_tools()
elif option == "2":
	run_scanning_and_enumeration_tools()
elif option == "3":
	run_exploitation_and_techniques_tools()
elif option == "4":
	run_post_exploitation_tools()
elif option == "5":
	generate_report()
else:
	print("Invalid option selected.")

if name == "main":
main()
