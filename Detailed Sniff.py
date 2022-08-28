#IMPORT
import scapy.all as scapy
from scapy.layers import http
from colorama import *
import sys
import time
import os

#SLOWPRINT
def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1./6)

init()

#STARTING
slowprint("Starting...")
time.sleep(1)
os.system('cls')


#LOGO
time.sleep(2)
print(Fore.LIGHTMAGENTA_EX+""" __    __  .______       __              _______..__   __.  __   _______  _______ 
|  |  |  | |   _  \     |  |            /       ||  \ |  | |  | |   ____||   ____|
|  |  |  | |  |_)  |    |  |           |   (----`|   \|  | |  | |  |__   |  |__   
|  |  |  | |      /     |  |            \   \    |  . `  | |  | |   __|  |   __|  
|  `--'  | |  |\  \----.|  `----.   .----)   |   |  |\   | |  | |  |     |  |     
 \______/  | _| `._____||_______|   |_______/    |__| \__| |__| |__|     |__|     
By Funways_Antonin#1046                                                                                 
                                                                                  """)
time.sleep(3)

#SNIFFING
slowprint("Sniffing in progress...")
def sniffing(interface):
    scapy.sniff(iface=interface, store=False, prn=process_packet)

def process_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        print(packet.show())

sniffing('Wi-Fi')
