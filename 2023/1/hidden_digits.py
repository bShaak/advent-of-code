# combine the first digit with the last digit (in order) to make the line value
# iterate through lines
# each line: iterate through string char by char
# convert strings of digits into digits by constructing a new string as we parse the current line
# find first digit from start of string
# find first digit from end of string (backwards)
# combine the two once the end of the line is reached

# 1eightwo -> 182
# map indexes to digits, then combine at the end
import re

regex = r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))"

numberdict = {"one": "1","two": "2","three": "3","four": "4","five": "5","six": "6","seven": "7","eight": "8","nine": "9"}

def map_number(num: str):
  return numberdict.get(num, num)

with open('input.txt') as fp:
  sum = 0
  for line in fp:
    matches = re.finditer(regex, line)
    results = [map_number(match.group(1)) for match in matches]
    d = ''.join(results)
    calibration = f"{d[0]}{d[-1]}"
    sum = sum + int(calibration)
    print(f"{line} -> {results} -> {calibration} -> sum: {sum}")
    
  print(sum)