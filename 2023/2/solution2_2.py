# get the max of each cube colour for each game and multiply them together to get the power.
# sum the powers of all games.
game_max = {"red": 0, "green": 0, "blue": 0}
power = 0
with open('input.txt') as fp:
  sum = 0
  valid_games = []
  for line in fp:
    game_max["blue"] = 0
    game_max["red"] = 0
    game_max["green"] = 0
    i = line.find(":")
    turns = line[i+2:].split("; ")
    for turn in turns:
      cubes = turn.split(", ")
      for cube in cubes:
        cube_count = cube.split(" ")
        colour = cube_count[1].strip()
        count = int(cube_count[0])
        # get max for each color
        if(count > game_max.get(colour)):
          game_max[colour] = count
    power = game_max["red"] * game_max["green"] * game_max["blue"]
    sum = sum + power
  print(sum)