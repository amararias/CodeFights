# Check if all digits of the given integer are even.

# Example

# For n = 248622, the output should be
# evenDigitsOnly(n) = true;
# For n = 642386, the output should be
# evenDigitsOnly(n) = false.
def evenDigitsOnly(n):
    return sum([int(x)%2 for x in str(n) if int(x)%2!=0])==0

n = 248623
print(
    evenDigitsOnly(n)
    )