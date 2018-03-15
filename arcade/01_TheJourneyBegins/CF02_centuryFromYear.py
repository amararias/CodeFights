# Given a year, return the century it is in. The first century spans from the year 1 up to and including the year 100, the second - from the year 101 up to and including the year 200, etc.

# Example

# For year = 1905, the output should be
# centuryFromYear(year) = 20;
# For year = 1700, the output should be
# centuryFromYear(year) = 17.

def centuryFromYear(year):
    year_s = str(year)
    year_len = len(year_s)

    if year_len <= 2 or year == 100:
        return 1    
    elif year_len == 3:
        if year_s[-2:] == "00":
            return int(year_s[0])
        else:
            return int(year_s[0]) + 1
    elif year_len == 4:
        if year_s[-2:] == "00":
            return int(year_s[:2])
        else:
            return int(year_s[:2]) + 1

for numero in [1, 2, 100, 101, 200, 501, 1000, 1001, 2015, 1999]:
    print(numero, ':', centuryFromYear(numero))