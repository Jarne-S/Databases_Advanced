# Databases_Advanced

## Virtual Machine:
	Installatie Ubuntu Virtual Machine (python 3 is hierbij inbegrepen): ubuntu-20.04.3-desktop-amd64

## Uitleg MongoDB & MongoDB Compass:
	Installatie: zie bash script.

## Uitleg webscraper:
	Installatie bs4 commando: sudo apt-get install python3-bs4
	Installatie pymongo commando: sudo apt-get install python3-pymongo
	Webscraper-script runnen via terminal commando: python3 webscraper.py

## Output: 
	Een log tekstbestand met de data van de grootste transactie per minuut met de data: datum, tijd, bitcoinhash, transactiewaarde in bitcoin en transactiewaarde in US Dollar.
	MongoDB database genaamd "Transactions" met 2 collecties:
		- Collectie 1 genaamd "all_transactions": bevat per minuut een document met alle transacties van die minuut.
		- Collectie 2 genaamd "biggest_transactions": bevat per minuut een document met de grootste transactie van die minuut
