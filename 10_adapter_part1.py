from collections import Counter

file = "input_files/problem10.txt"


data = []
with open(file, "r") as f:
    for line in f:
        l = int(line.replace("\n", ""))
        data.append(l)

print(data)

# first sort
ds = sorted(data)

# add charging outlet to front
ds = [0] + ds

i = 1
diffs = []
while i < len(ds):
    diffs.append(ds[i] - ds[i-1]) 
    i += 1

# add last 3 volt diff
diffs.append(3)

assert any([x>3 for x in diffs]) == False

c = Counter(diffs)
print(c)
answer = c[1] * c[3]
print(f"the answer to part 1 is {answer}")