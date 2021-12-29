import re
import math

file = "input_files/problem12.txt"

with open(file, "r") as f:
    data = f.read()

directions = data.split("\n")
print(directions)


parser = re.compile("(N|S|E|W|L|R|F)(\d+)")

detailed_instructions = []
for d in directions:
    m = parser.match(d)
    detailed_instructions.append((m.group(1), int(m.group(2))))


# make sure all turns are multiples of 90

rotations = [(i,r) for i,r in detailed_instructions if i in ("R", "L")]
non_90_rotators = [(i,r) for i,r in rotations if r % 90 != 0]
assert len(non_90_rotators) == 0


# use (x,y) cartesian coordinates
# ship faces E
# N is 0, E is 90, S is 180, W 270, and so forth

facing = 90

x, y = 0,0 

map_facing_to_dir = {
    0: 'N',
    90: 'E',
    180: 'S',
    270: 'W'
}

for i, u in detailed_instructions:
    if i == 'F':
        # figure out direction and it will move based on the instr below
        i = map_facing_to_dir[facing]


    # handle all instr except F
    if i == 'N':
        y += u
    elif i == 'E':
        x += u 
    elif i == 'S':
        y -= u 
    elif i == 'W':
        x -= u
    elif i == 'R':
        facing = (facing + u) % 360
    elif i == 'L':
        facing = (facing + 360 - u) % 360 
    


def manhattan_distance(x, y):
    return abs(x) + abs(y)


part1answer = manhattan_distance(x,y)
print(f"The answer to part 1 is {part1answer}")
