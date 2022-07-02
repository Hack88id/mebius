import os
import time
import re

time.sleep(3)
print ("\033[1;31m")

k = ("""
           ,__,
           (oo)____
           (__)    )\\
              ||--|| *

     [*]ZHF31 mebius 13FHZ[*]
""")

print(k)

while True:
	t = input ("\033[1;31mZHF31 >> \033[1;0m")
	if t not in("help","clear","ddos","wl","bffb","bfins","info",""," ","exit","keluar",):
		print ("comman",t,"not found")
		print ("type `help` to show command")
	if t =="help":
		print("""
comman      fungsi
------      ------
help        memunculkan bantuan
clear       bersihkan layar
wl          membuat wordlist
ddos        ddos web
bffb        bruteforce facebook
bfins       bruteforce instagram
info        info os
""")
	elif t =="clear":
		os.system("clear")
		os.system("python z.py")
	elif t =="wl":
		os.system('python2 wlt.py')
	elif t =="ddos":
		print ("""
	Hammer Dos Script v.1 http://www.canyalcin.com/
        It is the end user's responsibility to obey all applicable laws.
        It is just for server testing script. Your ip is visible.

        usage : python3 hammer.py [-s] [-p] [-t]
        -h : help
        -s : server ip
        -p : port default 80
        -t : turbo default 135
""")
		ip = input("[!] > ")
		os.system(ip)
	elif t =="info":
		print ("""
          OS INFO

AUTHOR       : TS HACKER
GITHUB       : Hack88id
TEAM         : INDO HACK TEAM
MADE A DATE  : 18/06/2022
""")
	elif t =="bffb":
		os.system('python faceboom.py')
		bffb = input("[>] ")
		os.system(bffb)
	elif t =="bfins":
		os.system('python3 insta.py')
