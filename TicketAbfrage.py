
import requests
from getpass import getpass
import re
import time

name = input("Name: ")

pwd = getpass()
run = 1
while True:
    print(run)
    run += 1
    # request an die Login Seite, um Login Code (ta_id) zu bekommen
    url = "https://wlan-login.oszimt.de/logon/cgi/index.cgi"
    req = requests.post(url, allow_redirects=False, data={})
    htmlAntwort = req.text  # HTML Antowrt der Seite in Variable speichern
    x = re.findall('\"[\d\D]{32}\s[\d\D]{32}\"', htmlAntwort) #ta_id hat 2 32 Bit Hex-Felder, die durch Leerzeichen getrennt sind, " sorgt für genau diesen gesuchten Text ohne andere Werte
    print(x) # Ausgabe des Arrays von re.findall
    if(len(x) == 0): #Wenn Array leer -> Ticket noch gültig -> muss nicht neu anmelden
        time.sleep(10) #Zeit, die zwischen Abfragen liegen soll
        continue
    else: # Neuanmeldung initiieren
        x[0] = x[0].replace('"', "") #wenn Array Wert enthält, dann nur mit "Code" -> für senden müssen Daten ohne " sein
    print(x) #ausgabe des Arrays, nur zur Kontrolle
    # print(htmlAntwort)
    url = "https://wlan-login.oszimt.de/logon/cgi/index.cgi#anchor_voucherLogon"
    req = requests.post(url, allow_redirects=False, data={
        'uid': name,
        'pwd': pwd,
        'ta_id': x[0],
        'voucher_logon_btn': True
    })
    
