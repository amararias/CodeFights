# You have a string s that consists of English letters, punctuation marks, whitespace characters, and brackets. It is guaranteed that the parentheses in s form a regular bracket sequence.

# Your task is to reverse the strings contained in each pair of matching parentheses, starting from the innermost pair. The results string should not contain any parentheses.

# Example

# For string s = "a(bc)de", the output should be
# reverseParentheses(s) = "acbde".

def findParentheses(s):
    start = s.index("(")
    end = len(s) - s[::-1].index(")") - 1
    print("-" * 80)
    print("original string: ", s)
    print("string found: ", s[start + 1:end])
    rev_s = s[end-1:start:-1]
    rev_s = rev_s.replace('(', ')', 1)
    rev_s = rev_s.replace(')', '(', 1)
    print("reversed string: ", rev_s)
    return (start, end, rev_s)

def reverseParentheses(s):
    (i, j, sNew) = findParentheses(s)
    while i != -1:
        print(sNew)
        (i, j, sNew) = findParentheses(sNew)


s = "a(bcdefghijkl(m(no)p))q"
print(reverseParentheses(s))


# s: "a(bcdefghijkl(mno)p)q"

# Expected Output:
# "apmnolkjihgfedcbq"