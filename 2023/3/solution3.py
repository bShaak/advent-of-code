# read input and insert into a 2D matrix
# iterate over the matrix, as we read in a symbol, launch a search around the symbol for digits.
# add the digits to a dictionary that contains key,val of {range,digit} where range is i1,j1-i2,j2. This will eliminate any duplicates.
# at the end, iterate over the dictionary and add them all up or whatever.
h = 140
w = 140

def is_symbol(val: str):
  if(val.isdigit()):
    return False
  if(val == "."):
    return False
  return True

# look in +i and -i direction for more digits and add them to the dict
def get_digit(digit_dict, matrix, j, i):
  if(j < 0 or j >= h or i < 0 or i >= w or matrix[j][i].isdigit() == False):
    return
  
  digit = matrix[j][i]
  a = i-1
  while(a >= 0 and matrix[j][a].isdigit()):
    digit = matrix[j][a] + digit
    a -= 1

  b = i+1
  while(b < w and matrix[j][b].isdigit()):
    digit += matrix[j][b]
    b += 1
  key = str(a) + "," + str(j) + "-" + str(b) + "," + str(j)
  digit_dict[key] = digit

# TODO: just call get_digit in a loop over -1 +1 for i,j
def find_digits(digit_dict, matrix, j, i):
  y = j - 1
  while(y < j + 2):
    x = i - 1
    while(x < i + 2):
      get_digit(digit_dict, matrix, y, x)
      x += 1
    y += 1

digit_dict = {}
matrix = [["." for x in range(w)] for y in range(h)]
with open("/Users/bradenshaak/learn/advent/advent-of-code/2023/3/input.txt") as file:
  y = 0
  for line in file:
    x = 0
    for char in line:
      if(char != "\n"):
        matrix[y][x] = char
        x = x + 1
    y = y + 1
  
  # use matrix from here
  for j in range(h):
    for i in range(w):
      val = matrix[j][i]
      if(is_symbol(val)):
        find_digits(digit_dict, matrix, j, i)
  # add up all the digits or whatever
  sum = 0
  for key, value in digit_dict.items():
    sum += int(value)
  print(sum)


