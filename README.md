# WLAN-Autoanmeldung
OSZIMT reconnect bei aufgebrauchtem Ticket

Das Skript fragt in regelmäßigen Abständen den Server nach dem Ticket-Status ab.
Wenn das Ticket noch gültig ist (weniger als 1000 mb verbraucht), gibt es kein login Fenster, sondern lediglich Ticketinformationen. Sollte das Ticket aufgebraucht sein, wird das Login-Fenster vom Server geliefert.
Das Formular enthält eine ID in Hex-Code. Diese wird  mittels RegEx ausgelesen und dann in einem Request mit Nutzername und Passwort an die Action-Seite des Formulars weitergegeben. Danach sollte der Login erfolgen.
Sofern Nutzername oder Passwort falsch sein sollten, bricht das Skript automatisch nach dem dritten Loginversuch ab.

## Features
- anzeige der aktuell verbrauchten MB
- Zeit zwischen Abfragen einstellbar (aktuell 10 Sekunden)
- schneller reconnect bei abgelaufenem Ticket

# Benötigte Module
- requests
- time
- getpass
- re


## Eventuelle Features
- GUI

