import pprint

pp = pprint.PrettyPrinter(indent=4)

numrows = 128  # 0 to 127


def read_input(inputfile):
    output = []
    with open(inputfile, "r") as f:
        for line in f:
            line = line.strip().replace("\n", "")
            output.append(line)
    return output


def findrow(ticket_front):
    """takes a ticket and num chars, ie 7 is 2**7 or 128 possible seats
    F means front and B means back in the binary search"""
    numchars = 7
    low = 0
    high = 2 ** numchars
    arr = list(range(high))
    numdivides = 0
    while numdivides < numchars:
        instruction = ticket_front[numdivides]
        mid = low + (high - low) // 2
        if instruction == "F":
            high = mid
        else:
            low = mid
        numdivides += 1
    return arr[low]


def findcol(ticket_back):
    numchars = 3
    low = 0
    high = 2 ** numchars
    arr = list(range(high))
    numdivides = 0
    while numdivides < numchars:
        instruction = ticket_back[numdivides]
        mid = low + (high - low) // 2
        if instruction == "L":
            high = mid
        else:
            low = mid
        numdivides += 1
    return arr[low]


def process_ticket(ticket):
    ticket_front = ticket[:7]
    ticket_back = ticket[7:]
    row = findrow(ticket_front)
    col = findcol(ticket_back)
    return row * 8 + col


if __name__ == "__main__":
    inputfile = "input_files/problem5.txt"
    tickets = read_input(inputfile)

    choice = input("press 1 or 2 to run part 1 or part 2\n")
    if not choice in ("1", "2"):
        raise ValueError("pick 1 or 2")

    if choice == "1":
        largest = 0
        for ticket in tickets:
            largest = max(largest, process_ticket(ticket))

        print(f"The largest ticket is {largest}")

    if choice == "2":
        ticketed_seats = set()
        for ticket in tickets:
            ticketed_seats.add(process_ticket(ticket))

        all_seats = set(range(128*8))

        missing = list(all_seats - ticketed_seats)

        counter = 1
        # missing seat is the first seat that is not adjacent to beginning
        while counter < len(missing):
            if missing[counter] - 1 > missing[counter-1]:
                print(f"the answer to part 2 is {missing[counter]}")
                break
            counter += 1





