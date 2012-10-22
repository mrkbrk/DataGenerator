
import sys
import csv
import random

def getRandomRow(lst):
    row = []
    rowSize = len(lst[0])
    errorProbability = len(lst) * rowSize
    for i in range(0,rowSize):
        rowIndex = random.randint(0, len(lst)-1)
        element = lst[rowIndex][i]
        if errorChance(errorProbability):
            element = generateError(element)
        row.append(element)
    return row

def errorChance(size):
    actual = random.randint(0,size)
    chance = size*0.95
    if actual>chance:
        return True
    else: return False

def generateError(element):
    if isinstance(element,int):
        element *= -1
    else:
        element = ''.join(random.sample(element,len(element)))
    return element
        
def getCsvContaint():
    csvInput = sys.argv[1]
    lst = []
    with open(csvInput, 'rb') as csvFile:
        dialect = csv.Sniffer().sniff(csvFile.read(1024))
        csvFile.seek(0)
        reader = csv.reader(csvFile, dialect)
        for row in reader:
            lst.append(row)
        return lst


def writeItemsToCsv(finalList):
    with open('out.cvs', 'wb') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(finalList)

def main():

    lst = getCsvContaint()
    print "Loaded CSV"
    count = int(sys.argv[2])
    finalList = []
    for i in range(0,count):
        finalList.append(getRandomRow(lst))
    print "Generated new CSV"
    writeItemsToCsv(finalList)
    print "Writen to out.csv"
    
if __name__ == '__main__':
    main()
    




