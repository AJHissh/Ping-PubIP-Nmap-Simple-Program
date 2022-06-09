import os 
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
     
    
def ping_map():
    choice = input("enter nmap or ping or pub-ip to run program:")

    if choice == "nmap":
        nmap_cmd()
    if choice == "ping":
        ping_cmd()
    if choice == "pub-ip":
        get_pub_id()
    if choice == "exit":
        exit()


while ping_map != 0:
    ping_map()

