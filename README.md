# WLAN-Autoanmeldung
OSZIMT reconnect bei aufgebrauchtem Ticket

Das Skript fragt in regelmäßigen Abständen den Server nach dem Ticket-Status ab.
Wenn das Ticket abgelaufen ist, dann wird auf die Login-Seite weitergeleitet, in der zwei 32-Bit lange Zeichenketten eingebettet sind, die zur Anmeldung benötigt werden. 
Mit diesen Daten wird ein Request an den Server geschickt, der dann die Anmeldung im Netzwerk verifiziert.

Wenn das Ticket noch gültig ist, enthält die Seite nicht die Zeichenkette -> das Ticket ist noch valide.

# benötigte Module
requests
time
getpass
re

