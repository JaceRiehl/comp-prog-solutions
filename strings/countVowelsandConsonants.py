def countVowelsAndConsonants(string, vowelList, consonantList):
    strList = list(string)
    countMap = {"vowelCount": 0, "consonantCount": 0}
    for char in strList:
        if char in vowelList:
            countMap["vowelCount"] = countMap["vowelCount"] + 1
        else: 
            countMap["consonantCount"] = countMap["consonantCount"] + 1
    return countMap

vowelList = {'a', 'e', 'i', 'o', 'u'}
consonantList = {'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'}
specialCharactersString = input("Input any string with special characters: ") 
countMap = countVowelsAndConsonants(specialCharactersString, vowelList, consonantList)
print("Vowels: " + str(countMap["vowelCount"]))
print("Consonants: " + str(countMap["consonantCount"]))     