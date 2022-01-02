file = "input_files/problem13.txt"

with open(file, "r") as f:
    lines = f.readlines()

target = int(lines[0].replace("\n", ""))
shuttles_raw = lines[1].replace("\t", "").split(",")

shuttles = [int(x) for x in shuttles_raw if x != 'x']
print(shuttles)



def closest_timestamp(target, shuttle):
    closest_before = target // shuttle * shuttle
    closest_after = closest_before + shuttle 
    return closest_after


closest_after = [closest_timestamp(target, s) for s in shuttles]
time_to_wait = [i - target for i in closest_after]
lowest = min(time_to_wait)
pos = time_to_wait.index(lowest)
bus_id = shuttles[pos]

print(f"the answer to part 1 is: {bus_id * lowest}")
