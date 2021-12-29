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


part1answer = l 

print(f"The answer to part 1 is {part1answer}")


# now iterate again - we know the list is all positive


checklist = []

with open(file, "r") as f:
    for line in f:
        l = int(line.replace("\n", ""))
        checklist.append(l)



# use two pointers, and l cannot equal r
l = 0
r = 1 

while r < len(checklist):
    total = sum(checklist[l:r+1])
    if total == part1answer:
        print("found contiguous range")
        break
    elif total < part1answer:
        r += 1
    else:
        l += 1
        # l cannot be r
        r = max(l+1, r)

# l and r are indexes of checklist
slice_we_care_about = checklist[l:r+1]
print(slice_we_care_about)
print(sum(slice_we_care_about))
assert sum(slice_we_care_about) == part1answer

part2answer = min(slice_we_care_about) + max(slice_we_care_about)
print(f"The answer to part 2 is {part2answer}")

