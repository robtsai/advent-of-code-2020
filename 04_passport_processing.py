import pprint

pp = pprint.PrettyPrinter(indent=4)

import re


passports_raw = []

curr_passport = []
with open("input_files/problem4.txt", "r") as f:
    for line in f:
        if line == "\n":
            passports_raw.append(curr_passport)
            curr_passport = []
        curr_passport.append(line.strip().replace("\n", ""))
    passports_raw.append(curr_passport)


passports = [" ".join(x) for x in passports_raw]

# part 1
patterns = [
    "byr:.+",
    "iyr:.+",
    "eyr:.+",
    "hgt:.+",
    "hcl:.+",
    "ecl:.+",
    "pid:.+",
]

regex = [re.compile(p) for p in patterns]

# part 2

patterns2 = [
    "( |^)ecl:(amb|blu|brn|gry|grn|hzl|oth)( |$)",
    "( |^)pid:[0-9]{9}( |$)",
    "( |^)hcl:#[0-9a-f]{6}( |$)",
    "( |^)byr:[0-9]{4}( |$)",
    "( |^)iyr:[0-9]{4}( |$)",
    "( |^)eyr:[0-9]{4}( |$)",
    "( |^)hgt:[0-9]+(cm|in)( |$)",
]

byr = re.compile("byr:([0-9]{4})")
iyr = re.compile("iyr:([0-9]{4})")
eyr = re.compile("eyr:([0-9]{4})")

hgt = re.compile("hgt:([0-9]+)(cm|in)")

def check_years(p):
    rules = {
        'byr': (byr, 1920, 2002),
        'iyr': (iyr, 2010, 2020),
        'eyr': (eyr, 2020, 2030)
    }

    for rule in rules.values():
        repattern, low, high = rule 
        yr = repattern.search(p).group(1)
        if not low <= int(yr) <= high:
            return False
    return True

def check_height(p):
    measure = hgt.search(p).group(1)
    unit = hgt.search(p).group(2)
    if unit == 'cm':
        return 150 <= int(measure) <= 193
    else:
        return 59 <= int(measure) <= 76



regex2 = [re.compile(pa) for pa in patterns2]


num_valid = 0
for p in passports:
    check = [1 for r in regex if r.search(p)]
    if sum(check) == 7:
        num_valid += 1

print(f"valid passports for part 1 are: {num_valid}")


num_valid2 = 0
for p in passports:
    check = [1 for r in regex2 if r.search(p)]
    if sum(check) == 7:
        if check_years(p) and check_height(p):
            num_valid += 1
            print('valid', p)
    else:
        print("invalid", p)

# there is a bug in part 2 - wrong answer

print(f"valid passports for part 2 are: {num_valid}")
