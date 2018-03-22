# Given a string, replace each its character by the next one in the English alphabet (z would be replaced by a).

# Example

# For inputString = "crazy", the output should be
# alphabeticShift(inputString) = "dsbaz".

def alphabeticShift(inputString):
    r = [chr(ord(c) + 1)  if ord(c)<122 else 'a' for c in inputString]
    return ''.join(r)

inputString = 'crazy'
print(alphabeticShift(inputString))