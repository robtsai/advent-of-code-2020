
def process_input(filepath):
    output = []
    curr = []
    with open(filepath, 'r') as f:
        for line in f:
            if line == '\n':
                output.append(curr)
                curr = []
            else:
                curr.append(line.strip().replace('\n', ''))
    output.append(curr)
    return output


def unique_questions(group):
    s = set()
    for response in group:
        for char in response:
            s.add(char)
    return len(s)


def everyone_answered(group):
    """for a group of responses, return number of qustions EVERYONE answered yes"""
    l = len(group)
    d = {}
    for response in group:
        for char in response:
            d[char] = d.get(char, 0) + 1
    return sum([1 for v in d.values() if v == l])


if __name__ == '__main__':
    inputfile = "input_files/problem6.txt"
    customs = process_input(inputfile)
    

    total = 0
    for group in customs:
        total += unique_questions(group)

    print(f"answer to part 1 is {total}")


    all_yes = 0
    for group in customs:
        all_yes += everyone_answered(group)

    print(f"answer to part 2 is {all_yes}")

    