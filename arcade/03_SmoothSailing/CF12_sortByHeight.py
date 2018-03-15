# Some people are standing in a row in a park. There are trees between them which cannot be moved. Your task is to rearrange the people by their heights in a non-descending order without moving the trees.

# Example

# For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
# sortByHeight(a) = [-1, 150, 160, 170, -1, -1, 180, 190].

def sortByHeight(a):
    import numpy as np
    c = np.array(a)
    c[c != -1] = sorted([i for i in a if i != -1])
    return list(c)

a = [-1, 150, 190, 170, -1, -1, 160, 180]
print(sortByHeight(a))


