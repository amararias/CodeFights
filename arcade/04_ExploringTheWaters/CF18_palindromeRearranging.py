# Given a string, find out if its characters can be rearranged to form a palindrome.

# Example

# For inputString = "aabb", the output should be
# palindromeRearranging(inputString) = true.

# We can rearrange "aabb" to make "abba", which is a palindrome.

def palindromeRearranging(s):
    if len(s)%2 == 0:
        for c in set(s):
            if s.count(c)%2 != 0:
                return False
    else:
        coun = []
        for c in set(s):
            if s.count(c)%2 != 0:
                coun.append(c)
        if len(coun) > 1:
            return False
    return True