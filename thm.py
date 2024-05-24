import subprocess
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-i", "--ip", dest="ip", help="IP Addr/hostname")
parser.add_argument('flags', nargs='?', help='Optional flags (a, n, g)')
args = parser.parse_args()

def nmap_scan():
	print("\n\n")
	print("_________________________Nmap Scan Details_________________________\n\n")
	type_scan=input("A/a for all port scan(-p-) or S/s for service scan(-sC,-sV) :  ")
	print("\n")
	match type_scan:
		case "A" | "a":
			print("all port scan it is on IP " + args.ip + "\n\n")
			scan_type="nmap -p- -T4 -vv "
		case "S" | "s":
			print("service scan it is on IP " + args.ip + "\n\n")
			scan_type="nmap -sC -sV -vv "
		case _:
			print("choose one of the above. \n\n")

	return subprocess.run(scan_type + args.ip, shell=True)

def gobuster_scan():
	print("\n\n_________________________Gobuster Scan Details_________________________\n\n")
	type_scan_gobuster=input("what type gobuster scan would you like dir, dns, or vhost :  ")
	print('\n1. common.txt\n2. big.txt\n3. small.txt \n')
	wordlist=input("which wordlist would you prefer (default: common.txt) : ")
	print('\n')
	extensions=input('any additional extensions other than php,txt: ')
	print('\n\n')
	match wordlist:
		case '1':
			wordlist_loc='/usr/share/wordlists/dirb/common.txt'
		case '2':
			wordlist_loc='/usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt'
		case '3':
			wordlist_loc='/usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-small.txt'
		case _:
			print('choose apt wordlist')
	match type_scan_gobuster:
		case "dir":
			if len(extensions)>2:
				scan_type_gobuster="gobuster dir -u "+ args.ip +" -w " + wordlist_loc + " -x php,txt," + extensions.strip()
			else:
				scan_type_gobuster="gobuster dir -u "+ args.ip +" -w " + wordlist_loc + " -x php,txt"
		case "dns":
			scan_type_gobuster="gobuster dns -d "+ args.ip + " -w Seclists/Discovery/DNS/subdomains-top1million-20000.txt"
		case "vhost":
			scan_type_gobuster="gobuster vhost -u " + args.ip + "-w Seclists/Discovery/DNS/subdomains-top1million-20000.txt"
		case _:
			print("choose appropriate method i.e dir, dns, vhost")	

	return subprocess.run(scan_type_gobuster, shell=True)

if 'a' in args.flags:
	nmap_scan()
	gobuster_scan()
if 'n' in args.flags:
	nmap_scan()
if 'g' in args.flags:
	gobuster_scan()
















