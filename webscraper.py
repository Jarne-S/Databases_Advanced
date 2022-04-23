import time
from numpy import full
import requests
from bs4 import BeautifulSoup
import datetime

def toevoegenCheck(huidigeTransactiesList , hash):
    nogNietToegevoegd = True
    for y in range(0,len(huidigeTransactiesList)):
            if hash == huidigeTransactiesList[y][0]:
                nogNietToegevoegd = False
    return nogNietToegevoegd

def grootsteTransactieVinden(transacties , datum):
    transactiewaarde = 0
    transactieindex = 0
    for x in range(0,len(transacties)):
        if float(transacties[x][3].replace("$" , "").replace(",","")) > transactiewaarde:
            transactiewaarde = float(transacties[x][3].replace("$" , "").replace(",",""))
            transactieindex = x
    resultaat = [datum, transacties[transactieindex][1] , transacties[transactieindex][0] , transacties[transactieindex][2] , transacties[transactieindex][3]]
    return resultaat

def tijdzone(timestamp):
    timestampSplit = timestamp.split(":")
    timestampSplit[0] = int(timestampSplit[0])+2
    if timestampSplit[0] >=24:
        timestampSplit[0] = str(timestampSplit[0]-24)

    if int(timestampSplit[0]) < 10:
        timestampSplit[0] = "0" + str(timestampSplit[0])
    newTimeStamp = str(timestampSplit[0]) + ":" + str(timestampSplit[1])
    return newTimeStamp

def dateformat(datum):
    datesplit = str(datum).split("-")
    newdate = datesplit[2] + "/" + datesplit[1] + "/" + datesplit[0]
    return newdate

starttime = time.time()

currentTransactionTime = ""
currentTransactionTimeTransactions = []
currentDate = datetime.date.today()

while True:
    # SCRAPING VAN DE WEBSITE
    url = "https://www.blockchain.com/btc/unconfirmed-transactions"
    request = requests.get(url)
    scrapesBS = BeautifulSoup(request.text , "html.parser")
    hashes = scrapesBS.find_all("div" , {"class": "sc-1g6z4xm-0 hXyplo"})
    hashes.reverse()

    # DATA CLEANING EN SAMENZETTEN
    Alldata = []
    for x in range(0, len(hashes)):
        hashcode = hashes[x].find("a" , {"sc-1r996ns-0 fLwyDF sc-1tbyx6t-1 kCGMTY iklhnl-0 eEewhk d53qjk-0 ctEFcK"}).get_text()
        OtherData = hashes[x].find_all("span" , {"class":"sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC"})
        
        TimeStamp = tijdzone(OtherData[0].get_text())
        BitcoinAmount = OtherData[1].get_text()
        DollarAmount = OtherData[2].get_text()
        Alldata.append([hashcode, TimeStamp , BitcoinAmount , DollarAmount])

    # DATA TOEVOEGEN / GROOTSTE ZOEKEN
    for x in range(0,len(Alldata)):
        tijdswaarde = int(Alldata[x][1].replace(":",""))
        datum = dateformat(currentDate)

        if currentTransactionTime == "":
            currentTransactionTime = tijdswaarde
            
            if toevoegenCheck(currentTransactionTimeTransactions, Alldata[x][0]):
                currentTransactionTimeTransactions.append(Alldata[x])
        
        elif tijdswaarde == currentTransactionTime:
            if toevoegenCheck(currentTransactionTimeTransactions, Alldata[x][0]):
                currentTransactionTimeTransactions.append(Alldata[x])

        elif (currentTransactionTime >= 2357) and (tijdswaarde <= 2):
            # Hoogste resultaat printen
            print(grootsteTransactieVinden(currentTransactionTimeTransactions , datum))
            resultaat = resultaat = "  ".join(grootsteTransactieVinden(currentTransactionTimeTransactions, datum))
            file = open("logs.txt" , "a")
            file.write(resultaat + "\n")
            #file.write("\n")
            file.close()
            currentTransactionTimeTransactions = []

            #nieuwe minuut van transacties opslagen & dag+1
            currentTransactionTime = tijdswaarde
            currentDate += datetime.timedelta(days=1)
            if toevoegenCheck(currentTransactionTimeTransactions, Alldata[x][0]):
                currentTransactionTimeTransactions.append(Alldata[x])

        elif(tijdswaarde >= 2357) and (currentTransactionTime <=2):
            currentTransactionTime = currentTransactionTime

        elif tijdswaarde > currentTransactionTime:
            # Hoogste resultaat printen
            print(grootsteTransactieVinden(currentTransactionTimeTransactions, datum))
            resultaat = resultaat = "  ".join(grootsteTransactieVinden(currentTransactionTimeTransactions, datum))
            file = open("logs.txt" , "a")
            file.write(resultaat + "\n")
            #file.write("\n")
            file.close()
            currentTransactionTimeTransactions = []

            #nieuwe minuut van transacties opslagen
            currentTransactionTime = tijdswaarde
            if toevoegenCheck(currentTransactionTimeTransactions, Alldata[x][0]):
                currentTransactionTimeTransactions.append(Alldata[x])