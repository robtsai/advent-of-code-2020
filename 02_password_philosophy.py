from collections import Counter


def process_file(somepath):
    """processes input"""
    logs = []
    with open(somepath, "r") as f:
        for line in f:
            rule, password = line.replace("\n", "").split(":")
            password = password.strip()
            logs.append((rule, password))
    return logs


def validate_line(rule, password):
    """parses rule like 1-3 a and checks if the password valid"""
    numrange, char = rule.split(" ")
    l, h = numrange.split("-")
    low, high = int(l), int(h)
    c = Counter(password)
    if not char in c:
        numoccurences = 0
    else:
        numoccurences = c[char]
    return low <= numoccurences <= high


def validate_line_part2(rule, password):
    """parses rule like 1-3 a and checks if the password valid"""
    numrange, char = rule.split(" ")
    l, h = numrange.split("-")
    low, high = int(l), int(h)
    # remember they want us to match on 1-index
    leftchar = password[low - 1]
    rightchar = password[high - 1]
    match_arr = [leftchar == char, rightchar == char]
    return sum(match_arr) == 1


logs = process_file("input_files/problem2.txt")


valid_passwords = []
for rule, password in logs:
    if validate_line(rule, password):
        valid_passwords.append((rule, password))

valid_passwords_part2 = []
for rule, password in logs:
    if validate_line_part2(rule, password):
        valid_passwords_part2.append((rule, password))

print(f"the answer to part 1 is {len(valid_passwords)}")
print(f"the answer to part 2 is {len(valid_passwords_part2)}")
