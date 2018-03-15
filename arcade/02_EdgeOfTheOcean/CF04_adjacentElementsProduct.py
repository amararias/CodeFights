# Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.

# Example

# For inputArray = [3, 6, -2, -5, 7, 3], the output should be
# adjacentElementsProduct(inputArray) = 21.

# 7 and 3 produce the largest product.


def adjacentElementsProduct(s):
    products = []
    for i in range(0, len(s)-1):
        products += [s[i] * s[i+1]]
    
    return(max(products))

def adjacentElementsProduct2(inputArray):
    return max([inputArray[i] * inputArray[i+1] for i in range(len(inputArray)-1)])


inputArray = [3, 6, -2, -5, 7, 3]
print(adjacentElementsProduct(inputArray))