import sys
import re


ruleregex = re.compile("mem\[(\d+)\] = (\d+)")

file = "input_files/problem14.txt"


class Rule:
    def __init__(self, mask, mem_location, mem_override):
        self.mask = mask
        self.mem_location = int(mem_location) 
        self.mem_override = int(mem_override) 

    def __str__(self):
        return f"Rule with mask: {self.mask} and overriding mem loc {self.mem_location} with value {self.mem_override}"


with open(file, "r") as f:
    data = f.read()

print(data)

def remove_blanks(alist):
    newlist = []
    for x in alist:
        if x not in (" ", ""):
            newlist.append(x)
    return newlist

d2 = data.split("mask = ")
d2.pop(0)
d3 = [x.split("\n") for x in d2]
d4 = [remove_blanks(x) for x in d3]


allrules = []
for entry in d3:
    mask = entry[0]
    rules = entry[1:]
    for rule in rules:
        if ruleregex.match(rule):    
            mem_location = ruleregex.match(rule).group(1)
            mem_override = ruleregex.match(rule).group(2)
            ruleobj = Rule(mask, mem_location, mem_override)
            allrules.append(ruleobj)

memory = {}

def bin36(n):
    return format(n, '036b')

def mask_to_zero(mask):
    l = ['1' if char == 'X' else '0' for char in mask]
    return ''.join(l)

def mask_to_set(mask):
    l = ['1' if char == '1' else '0' for char in mask]
    return ''.join(l)

def apply_mask(memloc, n, mask, memory):
    value = bin36(n)
    print(f"value is \n\t\t{value}")
    print(f"int value if {n}")
    print(f"mask is \n\t\t{mask}")
    andmask = mask_to_zero(mask)
    print(f"mask with 00s in range to replace: andmask \n\t\t{andmask}")
    andmaskint = int(andmask, 2)
    print(f"now we want to an bitwise AND on mask with our andmask")
    value_after_andmask_int = n & andmaskint
    print(value_after_andmask_int)
    value_after_andmask = bin36(value_after_andmask_int)
    print(f"the value after applying andmask is \n\t\t{value_after_andmask}")
    print(f"now the ormask is the mask with 0s everywhere and 1s to override and set")
    or_mask = mask_to_set(mask)
    print(f"\n\t\t{or_mask}")
    print(f"now we OR this mask to get final result")
    final_result_int = int(or_mask, 2) | value_after_andmask_int
    print(f"final result as int is {final_result_int}")
    final_result = bin36(final_result_int)
    print(f"final result as mask is \n\t\t{final_result}")
    print(f"setting memory dict location {n} with value {final_result_int}")
    memory[memloc] = final_result_int
    return



for i, ruleobj in enumerate(allrules):
    print(f"processing {i}")
    apply_mask(ruleobj.mem_location, ruleobj.mem_override, ruleobj.mask, memory)



answer = sum(memory.values())
print(f"the answer to part 1 is {answer}")
