def reverseString(inputString):
    inputList = list(inputString)
    startingIndex = 0
    endingIndex = len(inputList) - 1
    while startingIndex < endingIndex:
        inputList = swapChars(inputList, startingIndex, endingIndex)
        startingIndex += 1
        endingIndex -= 1
    return ''.join(inputList)

def swapChars(inputList, startingIndex, endingIndex):
    tempChar = inputList[startingIndex]
    inputList[startingIndex] = inputList[endingIndex]
    inputList[endingIndex] = tempChar
    return inputList


print(reverseString(input("What string would you like reversed: ")))

