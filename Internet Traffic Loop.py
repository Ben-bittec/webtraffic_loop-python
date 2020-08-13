#!/usr/bin/env python
# coding: utf-8

#written by s1ck0

from subprocess import Popen
import os
import time
import webbrowser

cycles=int(input("Please input the number of cycles you want to run"))
num=int(input("Please input the number of pages you want to open in each cycle"))
delay1=int(input("Please input the time delay for restarting the cycle"))
delay2=int(input("Please input the time delay for Changing the IP"))
website = input("Please input your web address")

hits=cycles*num
print("You will access " +website+ " " , hits, " times")

for i in range(cycles):
    for i in range(num):
        webbrowser.open(website)
    time.sleep(delay1)
    print ("Killprocess Initiated")
    os.system("killall chrome")
    print("Chrome Killed")
    print("IP Change Initiated")
    os.system("sudo anonsurf change")
    time.sleep(delay2)
    print("IP Changed")

