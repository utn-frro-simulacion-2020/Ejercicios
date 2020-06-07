from utils import clearScreen
import re
import urllib.request


def getText():
    try:
        fp = urllib.request.urlopen("https://www.reddit.com/new")
    except:
        return getText()
    else:
        mybytes = fp.read()
        mystr = mybytes.decode("utf8")
        fp.close()

        pattern="(<h3.*?>)(.*)(</h3>)"
        g=re.search(pattern,mystr)
        return g.group(2)


def xorOne(string):
    newString = ''
    for i in range(0,int(len(string)/2)):
        newString += str(int(string[i]) ^ int(string[-(i+1)]))
    return newString


def xorTwo(string):
    newString = ''
    for i in range(1,len(string)):
        newString += str(int(string[i-1]) ^ int(string[i]))
    return newString


def randomNumberGenerator(nReturn):
    for i in range (0, nReturn):
        clearScreen()
        print("El generador se encuentra en ejecución")
        print(str(i) + " de " + str(nReturn) + " números generados.")
        print("Para visualizar el resultados abra el archivo numbers.txt")
        while True:
            text = getText()
            binary = ''.join(format(ord(i), 'b') for i in text)

            binary = xorOne(binary)
            binary = xorTwo(binary)
            binary = xorOne(binary)
            binary = xorTwo(binary)

            totalBcd = ""
            for i in range(0, len(binary) // 4):
                newSubstring = binary[slice(i*4, i*4 + 4)]
                newBcd = int(newSubstring, 2)
                if newBcd <= 9:
                    totalBcd += str(newBcd)

            if len(totalBcd) >= 4:
                number = "0."+totalBcd[slice(0, 4)]
                f = open("numbers.txt","a+")
                f.write(str(number) + "\n")
                f.close()
                break


def getDataSet():
    randomList = []
    with open("dataset.txt") as f:
        randomList = f.readlines()
        randomList = [x.strip() for x in randomList]
        for i in range(0, len(randomList)):
            randomList[i] = float(randomList[i])
    return randomList
