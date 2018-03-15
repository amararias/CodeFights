# Given a rectangular matrix of characters, add a border of asterisks(*) to it.

# Example

# For

# picture = ["abc",
#            "ded"]
# the output should be

# addBorder(picture) = ["*****",
#                       "*abc*",
#                       "*ded*",
#                       "*****"]

def addBorder(picture):
  a = ['*' * (len(picture[0]) + 2)]
  return a + ['*' + row + '*' for row in picture] + a