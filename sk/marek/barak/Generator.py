
import sys
import csv
import random
import datetime

def getDayStringFromInt(day):
    if day == 0:
        return "Pondelok"
    elif day ==1:
        return "Utorok"
    elif day == 2:
        return "Streda"
    elif day == 3:
        return "Stvrtok"
    elif day ==4 :
        return "Piatok"
    elif day ==5:
        return "Sobota"
    elif day == 6:
        return "Nedela"
    else: return ""

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
    chance = size*0
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
        finalList = list()
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
    elif option == "i":
        print "Index"
        finalList = list()
        size = len(lst)
        hasList = list()
        for i in range(size):
            indexList = list()
            for j in range(len(header)):
                if header[j] == "id_cas":
                    rand = random.randint(1,1000)
                    indexList.append(rand)
                elif header[j] =="id_zamestnanec":
                        rand = random.randint(1,283)
                        indexList.append(rand)
                elif header[j] == "id_zakaznik":
                        rand = random.randint(1,534)
                        indexList.append(rand)
                elif header[j] == "id_tovar":
                        rand = random.randint(1,451)
                        indexList.append(rand)
                elif header[j] == "id_dodavatel" or header[j]=="vybavuje_dodavatel":
                        rand = random.randint(1,70)
                        indexList.append(rand)
                elif header[j] == "id_faktura":
                        rand = random.randint(1,1996)
                        indexList.append(rand)
                elif header[j] == "id_pobocka":
                        rand = random.randint(1,12)
                        indexList.append(rand)
            
            l = lst.pop(0)
            l.pop(0)
            if not hasList.__contains__(str(indexList)):
                hasList.append(str(indexList))
                s = list()
                for i in l:
                    if i != "":
                        s.append(i) 
                indexList.extend(s)
                finalList.append(indexList)
                
                
        finalList.insert(0, header)
        writeItemsToCsv(finalList)
    elif option == "d":
        dt = datetime.datetime.now()
        dates = list()
        for i in range(count):
            dt += datetime.timedelta(days=1)
            today = list()
            today.append(dt)
            today.append(dt.year)
            today.append(dt.month)
            today.append(dt.day)
            today.append(getDayStringFromInt(dt.weekday()))
            dates.append(today)
        writeItemsToCsv(dates)
        
        
if __name__ == '__main__':
    main()
    




