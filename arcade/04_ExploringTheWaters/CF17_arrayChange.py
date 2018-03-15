# You are given an array of integers. On each move you are allowed to increase exactly one of its element by one. Find the minimal number of moves required to obtain a strictly increasing sequence from the input.

# Example

# For inputArray = [1, 1, 1], the output should be
# arrayChange(inputArray) = 3.

def arrayChange(s):
    count = 0
    for i in range(len(s)-1):
        if s[i]>=s[i+1]:
            count += s[i]-s[i+1]+1
            s[i+1] = s[i]+1
    return count