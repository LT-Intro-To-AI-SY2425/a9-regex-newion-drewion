import re

# Assignment 8 Part I
# in each of the problems below the first parameter to re.compile is "REPLACE ME" your
# job is to replace this text with a regular expression that behaves as described by the
# comment and accompanying prints/tests

# problem 1
# should extract a match where the first group is the month, the second group the day
# and the third group the year
date_string = "November 9, 1982"
# Explanation:
# ([a-z]+) : Group 1: Matches one or more letters (for the month). Case-insensitive due to re.IGNORECASE.
# \s+       : Matches one or more whitespace characters (the space after the month).
# (\d+)     : Group 2: Matches one or more digits (for the day).
# ,         : Matches the literal comma.
# \s+       : Matches one or more whitespace characters (the space after the comma).
# (\d{4})   : Group 3: Matches exactly four digits (for the year).
pat = re.compile(r"(\w+)\s+(\d+),\s+(\d{4})", re.IGNORECASE)
date_matches = pat.match(date_string)

# problem 2
# should extract a match where the first group is the number, the second the street, the
# third the city, the fourth the state and the fifth the zip code
address_string = "2501 Addison Street\nChicago, IL 60618"
# Explanation:
# (?P<number>\d+)    : Named Group 'number': Matches one or more digits at the start.
# \s+                : Matches one or more whitespace characters (space after number).
# (?P<street>.+)     : Named Group 'street': Matches any character (except newline by default) one or more times, until the newline.
# \s+                : Matches one or more whitespace characters (including the newline between street and city).
# (?P<city>[a-z]+)   : Named Group 'city': Matches one or more letters (for the city name). Case-insensitive.
# ,\s+               : Matches the literal comma followed by one or more whitespace characters.
# (?P<state>[a-z]{2}): Named Group 'state': Matches exactly two letters (for the state abbreviation). Case-insensitive.
# \s+                : Matches one or more whitespace characters (space before zip).
# (?P<zip>\d{5})     : Named Group 'zip': Matches exactly five digits (for the zip code).
pat = re.compile(r"(?P<number>\d+)\s+(?P<street>.+)\s+(?P<city>[\w]+),\s+(?P<state>[\w]{2})\s+(?P<zip>\d{5})", re.IGNORECASE)
address_matches = pat.match(address_string)

# problem 3
# should match all hashtags
tweet_string = "hi everyone! #cs #python #LT #champions"
# Explanation:
# #        : Matches the literal '#' character.
# (\w+)    : Group 1: Matches one or more alphanumeric characters (letters, numbers, and underscore).
#            re.findall returns only the captured group content when groups are present.
pat = re.compile(r"#(\w+)", re.IGNORECASE)
hashtag_matches = pat.findall(tweet_string)

# until you uncomment any code line below you'll get an EOF linting error feel free to
# ignore it
if __name__ == "__main__":
    print("<<<<< Date Problem >>>>>\n")
    # uncomment the following prints to see date results and asserts to test
    print(f"month is: {date_matches.group(1)}!") # should print "month is: November"
    print(f"day is: {date_matches.group(2)}!")   # should print "day is: 9"
    print(f"year is: {date_matches.group(3)}!")  # should print "year is: 1982"
    assert date_matches.group(1) == 'November', "Incorrect month"
    assert date_matches.group(2) == '9', "Incorrect day"
    assert date_matches.group(3) == '1982', "Incorrect year"
    print('\n<<<< Date extraction tests passed >>>>\n')

    print("<<<<< Address Problem >>>>>\n")
    # uncomment the following prints to see results and asserts to test
    print(f'number is: {address_matches.group("number")}!') # should print "number is: 2501"
    print(f'street is: {address_matches.group("street")}!') # should print "street is: Addison Street"
    print(f'city is: {address_matches.group("city")}!')     # should print "city is: Chicago"
    print(f'state is: {address_matches.group("state")}!')   # should print "state is: IL"
    print(f'zip is: {address_matches.group("zip")}!')       # should print "zip is: 60618"
    assert address_matches.group('number') == '2501', "Incorrect address number"
    assert address_matches.group('street') == 'Addison Street', "Incorrect street"
    assert address_matches.group('city') == 'Chicago', "Incorrect city"
    assert address_matches.group('state') == 'IL', "Incorrect state"
    assert address_matches.group('zip') == '60618', "Incorrect zip"
    print('\n<<<< Address extraction tests passed >>>>\n')

    print("<<<<< Hashtag Problem >>>>>\n")
    # uncomment the following prints to see results and asserts to test
    print(f"hashtags are: {hashtag_matches}") # should be ['cs', 'python', 'LT', 'champions']"
    assert hashtag_matches == ['cs', 'python', 'LT', 'champions'], "Incorrect hashtags"
    print('\n<<<< Hashtag extraction tests passed >>>>\n')

    print('\n<<<< All tests passed! >>>>')