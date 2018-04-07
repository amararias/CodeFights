# Given a string, output its longest prefix which contains only digits.

# Example

# For inputString="123aa1", the output should be
# longestDigitsPrefix(inputString) = "123".

def longestDigitsPrefix(s):
    out = []
    for c in s:
        if c.isdigit():
            out += c
        else:
            break
    return "".join(out)

   
inputString = "a1234"
print(longestDigitsPrefix(inputString))