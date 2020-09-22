
##################################################
#            for more information see            #
#  https://github.com/ich95/WLAN-Autoanmeldung/  #
##################################################

import requests
from getpass import getpass
import re
import time
import warnings
warnings.filterwarnings("ignore")

name = input("Name: ")
pwd = getpass()
delay = 5  # Zeit zwischen abfragen in Sekunden

run = 1
count = 0

while True:
    print('{:<4}'.format(run), end=" ")
    run += 1
    # request an die Login Seite, um Login Code (ta_id) zu bekommen
    url = "https://wlan-login.oszimt.de/logon/cgi/index.cgi"
    req = requests.post(url, allow_redirects=False, data={}, verify=False)
    htmlAntwort = req.text  # HTML Antowrt der Seite in Variable speichern
    # ta_id hat 2 32 Bit Hex-Felder, die durch Leerzeichen getrennt sind, " sorgt für genau diesen gesuchten Text ohne andere Werte
    x = re.findall('\"[\d\D]{32}\s[\d\D]{32}\"', htmlAntwort)
    # print(x)  # Ausgabe des Arrays von re.findall (Debug)
    if(len(x) == 0):  # Wenn Array leer -> Ticket noch gültig -> muss nicht neu anmelden
        used = re.findall('\d+,\d+', req.text)
        if len(used) == 0:
            pass
        else:
            print("Verbraucht: %s mb" % (used[0]))
        time.sleep(delay)  # Zeit, die zwischen Abfragen liegen soll
        count = 0  # count wieder auf null setzen, da sonst nach 3 reconnects sonst Skript abbricht
        continue
    else:  # Neuanmeldung initiieren
        # wenn Array Wert enthält, dann nur mit "Code" -> für senden müssen Daten ohne " sein
        x[0] = x[0].replace('"', "")
    print(x)  # ausgabe des Arrays (Debug)
    # print(htmlAntwort) #Ausgabe der Antwort (HTML Volltext) (Debug)
    # request an Action-Seite im Login Formular
    url = "https://wlan-login.oszimt.de/logon/cgi/index.cgi#anchor_voucherLogon"
    req = requests.post(url, allow_redirects=False, data={
        'uid': name,
        'pwd': pwd,
        'ta_id': x[0],
        'voucher_logon_btn': True
    }, verify=False)

    if len(x) != 0:
        count += 1

    if count > 2:
        print("Nutzername oder Passwort überprüfen")
        break
