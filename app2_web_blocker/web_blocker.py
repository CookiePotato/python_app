#!/usr/bin/env python3
# -*- coding: utf-8 -*
"""
Created on Wed Jul 31 15:32:46 2019

@author: vicky
"""

import time
from datetime import datetime as dt

hosts_temp = "hosts"
hosts_path = r"/private/etc/hosts"
redirect = "127.0.0.1"
website_list = ["https://www.facebook.com","https://www.youtube.com","dub119.mail.live.com"]

while True:    
    if dt(dt.now().year,dt.now().month,dt.now().day,16) < dt(dt.now().year,dt.now().month,dt.now().day,17):
        print("Working hours...")
        with open(hosts_path,'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        with open(hosts_path,'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print(dt(dt.now().year,dt.now().month,dt.now().day,8))
        print(dt(dt.now().year,dt.now().month,dt.now().day,16))
        print(dt.now())
    time.sleep(2)

