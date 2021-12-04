# looks like 2 sum problem

nums = []

with open("input_files/problem1.txt", "r") as f:
    for line in f:
        nums.append(line.strip().replace("\n", ""))

nums_int = [int(x) for x in nums]


def two_sum(arr, target):
    """takes a list and target, returns tuple of nums that add to target"""

    processed = set()

    for n in nums_int:
        diff = target - n
        if not diff in processed:
            processed.add(n)
        else:
            return ("success", (n, diff))
    return ("fail", (-1, -1))


def three_sum(arr, target):
    """takes a list and a target, returns a tuple of three elemnents that add to target"""
    for i in range(len(arr) - 2):
        firstnum = arr[i]
        msg, tup = two_sum(arr[i + 1 :], target - firstnum)
        if msg == "success":
            return ("success", (firstnum, tup[0], tup[1]))
    return ("fail", (-1, -1))


_, part1 = two_sum(nums_int, 2020)
print(f"Answer to part 1 is {part1[0] * part1[1]}")

_, part2 = three_sum(nums_int, 2020)
print(f"Answer to part 2 is {part2[0] * part2[1] * part2[2]}")
