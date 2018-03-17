# You are given an array of integers representing coordinates of obstacles situated on a straight line.

# Assume that you are jumping from the point with coordinate 0 to the right. You are allowed only to make jumps of the same length represented by some integer.

# Find the minimal length of the jump enough to avoid all the obstacles.

# Example

# For inputArray = [5, 3, 6, 7, 9], the output should be
# avoidObstacles(inputArray) = 4.

# Check out the image below for better understanding:
def checkValid(s, divisor):
    signal = True
    for num in s:
        if num % divisor == 0:
            signal = False
            break
    return signal
            
def avoidObstacles(s):
    l = []
    for i in range(2, max(s)+2):
        print(i)
        if checkValid(s, i):
            l.append(i)
    return min(l)

inputArray = [5, 3, 6, 7, 9]
print(avoidObstacles(inputArray))