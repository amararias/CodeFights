# Given array of integers, find the maximal possible sum of some of its k consecutive elements.

# Example

# For inputArray = [2, 3, 5, 1, 6] and k = 2, the output should be
# arrayMaxConsecutiveSum(inputArray, k) = 8.
# All possible sums of 2 consecutive elements are:

# 2 + 3 = 5;
# 3 + 5 = 8;
# 5 + 1 = 6;
# 1 + 6 = 7.
# Thus, the answer is 8.

def arrayMaxConsecutiveSum(s, k):
    s0 = sum(s[:k])
    m = s0

    for i in range(1, len(inputArray)-(k-1)):
        s1 = s0 - s[i-1] + s[i+k-1]
        s0 = s1
        m = max(m, s1)
    return m

inputArray = [2, 3, 5, 1, 6]
k = 2
print(arrayMaxConsecutiveSum(inputArray, k))
        

        