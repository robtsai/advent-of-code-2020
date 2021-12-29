import pprint

pp = pprint.PrettyPrinter(indent=4)

def get_data(path):
    instructions = []
    with open(path, "r") as f:
        for line in f:
            instructions.append(line.strip().replace("\n", ""))
    return instructions


def play_game(instructions):
    visited = [False for _ in range(len(instructions))]
    acc = 0
    pos = 0

    while not visited[pos]:
        instr, amt = instructions[pos].split(" ")
        amt_int = int(amt)
        visited[pos] = True
        if instr == "nop":
            pos += 1
        elif instr == "acc":
            acc += amt_int
            pos += 1
        elif instr == "jmp":
            pos += amt_int
        else:
            raise ValueError("unknown instruction")
    return acc


def clean_data(instructions):
    clean_instructions = []
    for line in instructions:
        instr, amt = line.split(" ")
        amt_int = int(amt)
        clean_instructions.append([instr, amt_int])
    return clean_instructions


def parse_move(success, keepgoing, pos, acc, swaps_left, visited, instructions):
    if pos >= len(instructions):
        raise ValueError("out of arr range")
    instr, amt = instructions[pos]
    print(pos, instr, amt)
    if pos == len(clean_instructions) - 1:  # last line
        if instr == "jmp" and swaps_left == 0:
            return [
                (False, False, pos, acc, swaps_left, visited, instructions)
            ]  # success, keepgoing, ...
        elif instr == "acc":
            return [(True, False, pos, acc + amt, swaps_left, visited, instructions)]
        elif instr == "nop":
            return [(True, False, pos, acc, swaps_left, visited, instructions)]
        elif instr == "jmp":
            # swap to nop
            return [(True, False, pos, acc, swaps_left - 1, visited, instructions)]

    if visited[pos]:  # loop
        return [(False, False, pos, acc, swaps_left, visited, instructions)]

    visited_copy = visited[:]
    visited_copy[pos] = True

    if instr == "acc":
        return [(False, True, pos + 1, acc + amt, swaps_left, visited_copy[:], instructions)]

    if swaps_left > 0:
        # greedy take and swap
        if instr == "nop":
            swap = (
                False,
                True,
                pos + amt,
                acc,
                swaps_left - 1,
                visited_copy[:],
            )  # turn to jmp
            leave = (False, True, pos + 1, acc, swaps_left, visited_copy[:], instructions)
            return [swap, leave]
        elif instr == "jmp":
            swap = (False, True, pos + 1, acc, swaps_left - 1, visited_copy[:], instructions)
            leave = (False, True, pos + amt, acc, swaps_left, visited_copy[:], instructions)
            return [swap, leave]
    else:  # no swaps left
        if instr == "nop":
            return [(False, True, pos + 1, acc, swaps_left, visited_copy[:], instructions)]
        elif instr == "jmp":
            return [(False, True, pos + amt, acc, swaps_left, visited_copy[:], instructions)]
        elif instr == "acc":
            return [(False, True, pos + 1, acc + amt, swaps_left, visited_copy[:], instructions)]


    raise ValueError("reached end path - check code")


def play_game2(instructions):
    success = False
    keepgoing = True 
    pos = 0
    acc = 0
    swaps_left = 1
    visited = [False for _ in range(len(instructions))]

    explore = []
    explore.append((success, keepgoing, pos, acc, swaps_left, visited, instructions))

    while len(explore) > 0:
        next_move = explore.pop()
        success, keepgoing, pos, acc, swaps_left, visited, instructions = next_move 
        if success:
            return acc
        if keepgoing:
            move_results = parse_move(success, keepgoing, pos, acc, swaps_left, visited, instructions)
            for result in move_results:
                explore.append(result)









if __name__ == "__main__":
    inputfile = "input_files/problem8.txt"
    instructions = get_data(inputfile)

    choice = input("Choose 1 or 2\n")
    if not choice in ("1", "2"):
        raise ValueError("please choose 1 or 2")

    if choice == "1":
        answer1 = play_game(instructions)
        print(f"The answer to part 1 is {answer1}")
    else:
        clean_instructions = clean_data(instructions)
        answer2 = play_game2(clean_instructions)
        print(f"the answer to part 2 is {answer2}")
