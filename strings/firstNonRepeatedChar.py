def findNonRepeatedChar (string):
    stringList = list(string)
    charMap = {}
    for char in stringList:
        if char not in charMap:
            charMap[char] = 1
        else:
            charMap[char] += 1
    for char in stringList:
        if charMap[char] == 1:
            return char

print(findNonRepeatedChar(input("String to analyze: ")))