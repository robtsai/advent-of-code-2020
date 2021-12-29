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



waypoint = [10, 1]

def rotate(i, u, waypoint):
    """ i is R or L, u is multiple of 90 - returns a new waypoint
    L by 90 is same as R by 270"""
    x, y = waypoint
    if i == "L":
        u = (360 - u) % 360 

    if u == 0:
        return [x, y]
    elif u == 90:
        return [y, -x]
    elif u == 180:
        return [-x, -y]
    elif u == 270:
        return [-y,  x]
    else:
        raise ValueError("bug?")


x, y = 0, 0

for i, u in detailed_instructions:   
    # handle all instr except F
    if i == 'N':
        waypoint[1] += u
    elif i == 'E':
        waypoint[0] += u
    elif i == 'S':
        waypoint[1] -= u 
    elif i == 'W':
        waypoint[0] -= u
    elif i == 'F':
        x += u * waypoint[0]
        y += u * waypoint[1]
    elif i in ("L", "R"):
        waypoint = rotate(i, u, waypoint)


def manhattan_distance(x, y):
    return abs(x) + abs(y)

part2answer = manhattan_distance(x,y)

print(f"The answer to part 2 is {part2answer}")
