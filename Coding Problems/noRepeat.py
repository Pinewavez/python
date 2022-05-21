# first non repeating charater in a string

def nonrepeat(theString):
    freq = {}
    for i in theString:
        freq[i] = freq.get(i, 0) + 1 #Populate the dictionary with each character frequency

    for j in theString:   #traverse the dictionary and return the first elemnt that occurs once
        if freq[j] == 1:
            return j
    return -1


print(nonrepeat("abcabcfds"))