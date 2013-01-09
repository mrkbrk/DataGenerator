
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
        
def getCsvContaint(csvInput):
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
        writer = csv.writer(csvFile,csv.excel)
        writer.writerows(finalList)

def main():
    csvInput = sys.argv[1]
    lst = getCsvContaint(csvInput)
    header = lst.pop(0);
    print header
    print "Loaded CSV"
    count = int(sys.argv[2])
    option = (sys.argv[3])
    print option
    if (option == "m"):
        finalList = []
        hasList = list()
        for i in range(0,count):
            randomRow = getRandomRow(lst)
            if not hasList.__contains__(str(randomRow)):
                hasList.append(str(randomRow))
                finalList.append(getRandomRow(lst))
        print "Generated new CSV"
        finalList.insert(0, header)
        writeItemsToCsv(finalList)
        print "Writen to out.csv"
    else:
        
        finalList = list()
        size = len(lst)
        hasList = list()
        for i in range(size):
            indexList = list()
            for j in range(len(header)):
                if header[j].lower() == "id_cas":
                    rand = random.randint(1,100)
                    indexList.append(rand)
                elif header[j].lower() =="id_zamestnanec":
                    rand = random.randint(1,100)
                    indexList.append(rand)
                elif header[j].lower() == "id_zakaznik":
                    rand = random.randint(1,100)
                    indexList.append(rand)
                elif header[j].lower() == "id_tovaru":
                    rand = random.randint(1,100)
                    indexList.append(rand)
                elif header[j].lower() == "id_dodavatel":
                    rand = random.randint(1,100)
                    indexList.append(rand)
                elif header[j].lower() == "id_faktura":
                    rand = random.randint(1,100)
                    indexList.append(rand)
            header.reverse()
            l = lst.pop(0)
            l.pop(0)
            indexList.extend(l)
            if not hasList.__contains__(str(indexList)):
                hasList.append(str(indexList))
                finalList.append(indexList)
        finalList.insert(0, header)
        writeItemsToCsv(finalList)
        
if __name__ == '__main__':
    main()
    




