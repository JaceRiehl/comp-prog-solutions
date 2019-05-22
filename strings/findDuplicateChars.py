def mapStringCharCounts(string):
    duplicateMap = {}
    charArray = list(string)
    for char in charArray:
        if char not in duplicateMap:
            duplicateMap[char] = 1
        else:
            duplicateMap[char] += 1
    return duplicateMap

def printDuplicateChars(charMap):
    for mapKey in charMap.keys():
        if charMap[mapKey] > 1: print("Duplicate: " + str(mapKey) + " : " + str(charMap[mapKey]))

printDuplicateChars(mapStringCharCounts(input("What string would you like counted ")))