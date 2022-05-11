# Databases_Advanced

### Links repo's
github url: https://github.com/Jarne-S/Databases_Advanced
dockerhub url: https://hub.docker.com/repository/docker/jarneschoolmeesters/firstimage

## Docker:
	Installatie voor ubuntu: zie bash script: "Docker_Install_Script.bash"
	
## MongoDB image in Docker:
	Commando: docker run -d --name mongo-Jarne -p 27888:27017 mongo

## Redis image in Docker:
	Commando: docker run -d --name redis-Jarne -p 8389:6379 redis

## Pythonimage met benodigde packages (2 opties):
### optie 1 - image importeren van dockerhub:
	Commando: docker pull jarneschoolmeesters/firstimage
### optie2 - image zelf maken:
	Navigeer in terminal naar de correcte map met de webscraper en Dockerfile.
	Commando: docker build -t jarneschoolmeesters/firstimage .

## Webscraper uitvoeren:
	Commando: docker run -d --name webscraper-Jarne --network=host jarneschoolmeesters/firstimage

## Output: 
	Een log tekstbestand met de data van de grootste transactie per minuut met de data: datum, tijd, bitcoinhash, transactiewaarde in bitcoin en transactiewaarde in US Dollar.
	MongoDB database genaamd "Transactions" met 2 collecties:
		- Collectie 1 genaamd "all_transactions": bevat per minuut een document met alle transacties van die minuut.
		- Collectie 2 genaamd "biggest_transactions": bevat per minuut een document met de grootste transactie van die minuut
	De MongoDB database kan bekeken worden mits installatie van MongoDB compass en te verbinden met de port uit het mongodb docker commando (port: 27888)

	Opmerking: Het logbestand en de terminal output zal niet zichtbaar zijn aangezien het bestand in de python image runt en niet lokaal op python.