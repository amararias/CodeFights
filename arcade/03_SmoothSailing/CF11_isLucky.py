# Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.

# Given a ticket number n, determine if it's lucky or not.

# Example

# For n = 1230, the output should be
# isLucky(n) = true;
# For n = 239017, the output should be
# isLucky(n) = false.

def isLucky(n):
    s_n = str(n)
    len_sum = int(len(str(n))/2)
    return sum([int(i) for i in s_n[:len_sum]]) == \
           sum([int(i) for i in s_n[len_sum:]])


n = 123501
print(isLucky(n))
