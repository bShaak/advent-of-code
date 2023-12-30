
# Determine which games would have been possible if the bag had been loaded with only 
# 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?

# open file, read line by line.
# For each line, there are multiple games separated by ';'
# determine whice games are possible with 12 red, 13 green, 14 blue
valid_dict = {"red": 12, "green": 13, "blue": 14}
with open('/Users/bradenshaak/learn/advent_of_code/2023/2/input.txt') as fp:
  game = 1
  sum = 0
  valid_games = []
  for line in fp:
    # chop off the game at the front
    i = line.find(":")
    turns = line[i+2:].split("; ")
    is_valid = True

    # get the red, blue green numbers for each turn
    for turn in turns:
      if not is_valid:
        break
      cubes = turn.split(", ")
      for cube in cubes:
        cube_count = cube.split(" ")
        colour = cube_count[1].strip()
        count = int(cube_count[0])
        if(count > valid_dict.get(colour, 0)):
          is_valid = False
          break
        # print(colour)
        # print(count)
    if is_valid:
      print(f"valid: {turns}")
      sum = sum + game
    else:
      print(f"invalid: {turns}")
    game = game + 1
    print(sum)
  print(sum)