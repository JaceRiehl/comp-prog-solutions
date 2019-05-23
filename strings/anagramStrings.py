def checkStringAnagrams(string1, string2):
    if(len(string1) != len(string2)): return False
    s1List = list(string1)
    s2List = list(string2)
    startingIndex = 0 
    endingIndex = len(s1List) - 1
    while(endingIndex != -1):
        print(endingIndex)
        if (not checkMatchingCharacters(s1List[startingIndex], s2List[endingIndex])): 
            return False 
        endingIndex -= 1
        startingIndex += 1
    return True
        

def checkMatchingCharacters(char1, char2):
    if(char1 != char2):
        return False
    return True

print("Strings are anagrams" + ": " + str(checkStringAnagrams(input("First string: "), input("Second string: "))))