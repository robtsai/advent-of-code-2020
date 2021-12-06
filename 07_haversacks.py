import re


valid_bag = re.compile("[0-9]+ (.+bag)")
target_bag = "shiny gold bag"


def process_input(file):
    output = {}
    with open(file, "r") as f:
        for line in f:
            # sample line
            # light red bags contain 1 bright white bag, 2 muted yellow bags.
            line = line.strip().replace("\n", "")
            parsed = line.split(" contain ")
            k = parsed[0]
            v = parsed[1].split(",")
            # make key singular
            k = k.replace("bags", "bag")
            targets = []
            for bag in v:
                if valid_bag.search(bag):
                    targets.append(valid_bag.search(bag).group(1))
            output[k] = targets
    return output


def traverse_graph(bag_rules):
    nodes = [x for x in bag_rules if x != target_bag]
    reachable = [1 for b in nodes if can_reach_target(b, bag_rules)]
    return sum(reachable)


def can_reach_target(bag, bag_rules):
    visited = {}  # do we need this to prevent cycles?

    to_visit = [bag]

    while len(to_visit) > 0:
        curr = to_visit.pop()
        visited[curr] = True
        next_bags = bag_rules.get(curr, [])
        for b in next_bags:
            if b == target_bag:
                return True
            if not b in visited:
                to_visit.append(b)
    return False


if __name__ == "__main__":
    file = "input_files/problem7.txt"
    bag_rules = process_input(file)
    print(f"the answer to part 1 is {traverse_graph(bag_rules)}")
