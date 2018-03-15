# Given an array of strings, return another array containing all of its longest strings.

# Example

# For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
# allLongestStrings(inputArray) = ["aba", "vcd", "aba"].

def allLongestStrings(inputArray):
    max_length =max(map(lambda x:len(x), inputArray))
    return list(filter(lambda s: len(s) == max_length, inputArray))

inputArray = ["aba", "aa", "ad", "vcd", "aba"]
inp = ["abaa", "aa", "ad", "vcd", "aba"]
print(allLongestStrings(inputArray))
print(allLongestStrings(inp))

