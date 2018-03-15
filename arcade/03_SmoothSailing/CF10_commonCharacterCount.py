# Given two strings, find the number of common characters between them.

# Example

# For s1 = "aabcc" and s2 = "adcaa", the output should be
# commonCharacterCount(s1, s2) = 3.

# Strings have 3 common characters - 2 "a"s and 1 "c".

def createDictionary(s):
    dictionary = {}
    for c in s:
        if c in dictionary:
            dictionary[c] += 1
        else:
            dictionary[c] = 1
    return dictionary

def commonCharacterCount(s1, s2):
    d1 = createDictionary(list(s1))
    d2 = createDictionary(list(s2))
    count = 0
    for k in d1.keys():
        try:
            count += min(d1[k], d2[k])
        except KeyError:
            pass
    return count



s1 = "aabcc"
s2 = "adcaa"
print(commonCharacterCount(s1,s2))