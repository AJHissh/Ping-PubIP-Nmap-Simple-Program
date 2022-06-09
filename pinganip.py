from ast import Return
import os 
import ctypes
import subprocess


def ping_cmd():
    ip = input("Please enter ip: ")  
    if ip is not None:
        print(ip)
        # cmd = f'ping -a -c {ip} -n 1 > /dev/null 2>&1' (for linux)
        cmd = f'ping -t -a {ip}'
        os.system(cmd)
    else:
        return ping_cmd()


def nmap_cmd():
    ip = input("Please enter ip: ")  
    if ip is not None:
        print(ip)
        # cmd = f'ping -a -c {ip} -n 1 > /dev/null 2>&1' (for linux)
        cmd = f'nmap -sV -A {ip}'
        os.system(cmd)
    else:
        return nmap_cmd()

def get_pub_id():
    subprocess.call('C:\Windows\System32\WindowsPowerShell/v1.0\powershell (Invoke-WebRequest ifconfig.me/ip).Content.Trim()', shell=True)
     
    
def ping_map():
    choice = input("enter nmap or ping or pub-ip to run program:")

    if choice == "nmap":
        nmap_cmd()
        return 1
    if choice == "ping":
        ping_cmd()
        return 1
    if choice == "pub-ip":
        get_pub_id()
        return 1

# count = ping_map

while ping_map != 0:
    ping_map()

