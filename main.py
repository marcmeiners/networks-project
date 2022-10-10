import csv
import numpy

totalBurstNumber = 0  

class Prefix():
    
    def __init__(self,timestamp,wab):
        global totalBurstNumber
        self.numberOfAnnouncements = 0
        self.numberOfWithdrawals = 0
        self.numberOfBursts = 0
        self.lastTimestamp = timestamp
        self.currentLength = 0
        self.burstOngoing = False
        self.longestBurst = 0
        self.totalLength = 0
        if wab == "A":
            self.numberOfAnnouncements = 1
        if wab == "W":
            self.numberOfWithdrawals = 1

    def addTimestamp(self,timestamp,wab):
        global totalBurstNumber
        if wab == "A":
            self.numberOfAnnouncements += 1
        if wab == "W":
            self.numberOfWithdrawals += 1
        if timestamp - self.lastTimestamp < 240:
            if self.burstOngoing:
                self.currentLength += timestamp - self.lastTimestamp
            else:
                self.currentLength = timestamp - self.lastTimestamp
                self.numberOfBursts += 1
                totalBurstNumber += 1
                self.burstOngoing = True
        else:
            if self.burstOngoing:
                self.burstOngoing = False
                self.totalLength+=self.currentLength
                if self.currentLength > self.longestBurst:
                    self.longestBurst = self.currentLength
                self.currentLength = 0
        self.lastTimestamp = timestamp    

def computeSolution(fileString, fileNumber):
    global totalBurstNumber 
    totalBurstNumber = 0   
    numberTotal = 0
    numberA = 0
    numberW = 0
    numberPreAnn = 0
    numberPreWith = 0
    maxNumberBursts = 0
    longestBurstTotal = 0
    numberNoBurst = 0
    avg10 = 0
    avg20 = 0
    avg30 = 0
    dict = {}

    with open(fileString, 'r') as file:
        reader = csv.reader(file, delimiter = '|')
        for row in reader:
            prefix = row[5]
            timestamp = int(row[1])
            wab = row[2]
            numberTotal+=1
            if wab == "A":
                numberA+=1
            if wab == "W":
                numberW+=1
            if prefix in dict:
                dict[prefix].addTimestamp(timestamp,wab)
            else:
                dict[prefix] = Prefix(timestamp,wab)

    averageBurstSummation = 0
    numberOfPrefixes = len(dict.keys())

    for x in dict:
        if dict[x].currentLength > 0:
            dict[x].totalLength += dict[x].currentLength
            if dict[x].currentLength > dict[x].longestBurst:
                dict[x].longestBurst = dict[x].currentLength
        if dict[x].numberOfAnnouncements > 0:
            numberPreAnn+=1
        if dict[x].numberOfWithdrawals > 0:
            numberPreWith+=1 
        if dict[x].numberOfBursts > maxNumberBursts:
            maxNumberBursts = dict[x].numberOfBursts
        if dict[x].longestBurst > longestBurstTotal:
            longestBurstTotal = dict[x].longestBurst
        if dict[x].numberOfBursts == 0:
            numberNoBurst += 1
        if dict[x].numberOfBursts > 0:
            if dict[x].totalLength / dict[x].numberOfBursts > 600:
                avg10 +=1
            if dict[x].totalLength / dict[x].numberOfBursts > 1200:
                avg20 +=1
            if dict[x].totalLength / dict[x].numberOfBursts > 1800:
                avg30 +=1

        averageBurstSummation += dict[x].longestBurst

    print("FILE",fileNumber)
    print("1: " + str(numberTotal))
    print("2: " + str(numberA))
    print("3: " + str(numberW))
    print("4: " + str(numberOfPrefixes))
    print("5: " + str(numberPreAnn))
    print("6: " + str(numberPreWith))
    print("7: " + str(totalBurstNumber))
    print("8: " + str(maxNumberBursts))
    print("9: " + str(longestBurstTotal))
    print("10: " + str(int(numpy.ceil(averageBurstSummation/numberOfPrefixes))))
    print("11: " + str(numberNoBurst))
    print("12: " + str(avg10))
    print("13: " + str(avg20))
    print("14: " + str(avg30))
    print("")

computeSolution("input/updates.20150613.0845-0945.csv",1)