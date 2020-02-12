from tkinter import *
import requests
import re
import time


def ticket():
    run = 1
    count = 0
    delay = 10

    while True:
        print(run, end=" ")
        run += 1
        output = str(run)
        Label(master, text="run:").grid(column=0, row=4, sticky=W, pady=4)
        Label(master, text=run).grid(column=1, row=4, sticky=W, pady=4)
        # request an die Login Seite, um Login Code (ta_id) zu bekommen
        url = "https://wlan-login.oszimt.de/logon/cgi/index.cgi"
        req = requests.post(url, allow_redirects=False, data={})
        # ta_id hat 2 32 Bit Hex-Felder, die durch Leerzeichen getrennt sind, " sorgt für genau diesen gesuchten Text ohne andere Werte
        x = re.findall('\"[\d\D]{32}\s[\d\D]{32}\"', req.text)
        # print(x)  # Ausgabe des Arrays von re.findall (Debug)
        if(len(x) == 0):  # Wenn Array leer -> Ticket noch gültig -> muss nicht neu anmelden
            used = re.findall('\d+,\d+', req.text)
            if len(used) == 0:
                pass
            else:
                print("Verbraucht: %s mb" % (used[0]))
                output = "verbraucht: "+str(x[0])+" mb"
                Label(master, text="verbrauchte mb: ").grid(
                    column=0, row=5, sticky=W, pady=4)
                Label(master, text=used[0]).grid(
                    column=1, row=5, sticky=W, pady=4)
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
            'uid': e1.get(),
            'pwd': e2.get(),
            'ta_id': x[0],
            'voucher_logon_btn': True
        })

        if len(x) != 0:
            count += 1

        if count > 2:
            print("Nutzername oder Passwort überprüfen")
            break


master = Tk()
master.geometry("250x160")
master.title("Ticket")
Label(master, text="Name").grid(row=0, sticky=W, pady=4)
Label(master, text="Passwort").grid(row=1, sticky=W, pady=4)

Label(master, text="run:").grid(column=0, row=4, sticky=W, pady=4)
Label(master, text="0").grid(column=1, row=4, sticky=W, pady=4)
Label(master, text="verbrauchte mb: ").grid(column=0, row=5, sticky=W, pady=4)
Label(master, text="0").grid(column=1, row=5, sticky=W, pady=4)
e1 = Entry(master)
e2 = Entry(master, show="*")

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)


Button(master, text='senden', command=ticket).grid(
    row=3, column=0, sticky=W, pady=4)
Button(master, text='beenden', command=master.quit).grid(
    row=3, column=1, sticky=W, pady=4)

mainloop()
