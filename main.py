import random
import string


def encrypt(text):
    lowercaseLetters = ""

    for letter in string.ascii_lowercase:
        lowercaseLetters += letter

    test = list(lowercaseLetters)
    random.shuffle(test)
    randomSubLower = ''.join(test)

    # print(uppercaseLetters)
    # print(randomSubUpper)
    # print(lowercaseLetters)
    # print(randomSubLower)

    encryptedMessage = ""
    indent = 0
    text = text.lower()
    for letter in text:
        indent += 1
        if letter in lowercaseLetters:
            index = lowercaseLetters.find(letter)
            encryptedMessage += randomSubLower[index]
        else:
            encryptedMessage += letter

    return encryptedMessage

    # randomSubLower =
    # for letter in text:

def indentMessage(text):
    message = []
    indent = 0
    for i in range(len(text)):
        if text[i] == " " and indent > 50:
            message.append(text[i-indent:i + 1])
            indent = 0
        indent += 1
    return message

def mostCommon(text):
    total = 0
    for letter in string.ascii_lowercase:
        letterAmount = text.count(letter)
        total += letterAmount

    freqList = []
    for letter in string.ascii_lowercase:
        amount = text.count(letter)
        percent = (amount / total * 100)
        percent = round(percent,2)
        freqList.append([letter,percent])

    for _ in range(len(freqList) - 1):
        for i in range(len(freqList) - 1):
            if freqList[i][1] < freqList[i + 1][1]:
                temp = freqList[i]
                freqList[i] = freqList[i + 1]
                freqList[i + 1] = temp

    for letter in freqList:
        print(f"{letter[0]} : {letter[1]}%")

def printMessage(message):
    for line in message:
        print(line)

def swapLetters(message):
    letterSwap = input("Input 2 Lettters(a(choose) b(replace)): ")
    letterSwap = letterSwap.lower()
    text = ""
    if len(letterSwap) == 2 and letterSwap[0] != letterSwap[1]:
        if letterSwap[0] in message:
            message = message.replace(letterSwap[0],"*")
            message = message.replace(letterSwap[1], letterSwap[0])
            message = message.replace("*", letterSwap[1])
            return message
    else:
        return message


def main():
    textInput = input("Input: ")
    text = encrypt(textInput)
    mostCommon(text)
    print(text)
    run = True
    newtext = text
    while run:
        newtext = swapLetters(newtext)
        mostCommon(newtext)
        print(newtext)
main()
