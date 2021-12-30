from collections import Counter

file = "input_files/problem10.txt"


data = []
with open(file, "r") as f:
    for line in f:
        l = int(line.replace("\n", ""))
        data.append(l)


# first sort
ds = sorted(data)
print(ds)

m = max(ds)
print(m)

numways = [0 for _ in range(m+1)]

numways[0] = 1


for i in ds:
    lookback = filter(lambda x: x >= 0, [i-1, i-2, i-3])
    ways_to_here = sum(numways[x] for x in lookback)
    numways[i] = ways_to_here


answer = numways[-1]

print(f"the answer to part2 is {answer}")