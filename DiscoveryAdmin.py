import os
from secrets import choice 
import subprocess


def ping_cmd():
    ip = input("Please enter ip: ")  
    if ip is not None:
        print(ip)
        cmd = f'ping -t -a {ip}'
        os.system(cmd)
    else:
        return ping_cmd()


def nmap_cmd():
    ip = input("Please enter ip: ")  
    if ip is not None:
        print(ip)
        cmd = f'nmap -sV -A {ip}'
        os.system(cmd)
    else:
        return nmap_cmd()

def get_pub_id():
    subprocess.call('C:\Windows\System32\WindowsPowerShell/v1.0\powershell (Invoke-WebRequest ifconfig.me/ip).Content.Trim()', shell=True)
    

def net_stat():
    print("Must run program with admin privileges, press enter to continue")
    wait = input("")
    if wait is not None:
        cmd = f'netstat -b'
        os.system(cmd)
    else:
        return net_stat()
    
def trace_ip():
    ip = input("Please enter ip or domain: ")  
    if ip is not None:
        print(ip)
        cmd = f'tracert {ip}'
        os.system(cmd)
    else:
        return trace_ip         
    
def ping_map():
    choice = input("## Choose nmap, ping, netstat, trace, pub-ip or exit ## : ")
    if choice == "nmap":
        nmap_cmd()
    if choice == "ping":
        ping_cmd()
    if choice == "pub-ip":
        get_pub_id()
    if choice == "netstat":
        net_stat()
    if choice == "trace":
        trace_ip()    
    if choice == "exit":
        exit()


while ping_map != 0:
    ping_map()

