# Given an array of integers, find the maximal absolute difference between any two of its adjacent elements.

# Example

# For inputArray = [2, 4, 1, 0], the output should be
# arrayMaximalAdjacentDifference(inputArray) = 3.

def arrayMaximalAdjacentDifference(s):
    return max([abs(s[i]-s[i+1]) for i in range(len(s) -1)])