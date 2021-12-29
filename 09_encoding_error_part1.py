from collections import deque

file = "input_files/problem09.txt"


d = deque([], maxlen=25)


def checksum(num, d):
    """checks that num can be made as sum of two numbers in d"""
    s = set()
    for n in d:
        if num - n in s:
            return True
        s.add(n)
    return False

with open(file, "r") as f:
    for line in f:
        l = int(line.replace("\n", ""))
        if len(d) == 25:
            if not checksum(l, d):
                break
        d.append(l)


print(f"The answer to part 1 is {l}")