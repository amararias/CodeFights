# Correct variable names consist only of English letters, digits and underscores and they can't start with a digit.

# Check if the given string is a correct variable name.

# Example

# For name = &quot;var_1__Int&quot;, the output should be
# variableName(name) = true;
# For name = &quot;qq-q&quot;, the output should be
# variableName(name) = false;
# For name = &quot;2w2&quot;, the output should be
# variableName(name) = false

def variableName(name):
    nums = '0123456789'
    valid_chars = 'abcdefghijqlmnopqrstuvwxyz'
    valid_chars = valid_chars + valid_chars.upper() + '_' + nums
    if name[0] in nums:
        return False
    for c in name:
        if c not in valid_chars:
            return False
    return True

name = '0variable0'
print(variableName(name))

  