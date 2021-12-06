import re


valid_bag = re.compile("[0-9]+ (.+bag)")
no_other_bag = re.compile("no other bags")
target_bag = "shiny gold bag"

valid_bag_2 = re.compile("([0-9]+) (.+bag)")


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


def process_input_qty(file):
    """reads file and accounts for numbers of bags
    returns dictionary of bag and list of tuples (bags contained, qty)"""
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
                if no_other_bag.search(bag):
                    continue
                elif valid_bag_2.search(bag):
                    qty = valid_bag_2.search(bag).group(1)
                    b = valid_bag_2.search(bag).group(2)
                    targets.append((b, int(qty)))  # save qty as int
            output[k] = targets
    return output


def traverse_graph(bag_rules):
    nodes = [x for x in bag_rules if x != target_bag]
    reachable = [1 for b in nodes if can_reach_target(b, bag_rules)]
    return sum(reachable)


# recurse


def count_downstream_bags(source_bag, num_cur, bag_qty_rules):
    # we start with x number of source_bag, and a bag_rules
    # this recursive function also includes counting the source bag
    children_bags = bag_qty_rules.get(source_bag, [])
    if not children_bags:
        return num_cur  # number of current bags with no children
    else:
        collector = []
        for b, qty in children_bags:
            res = count_downstream_bags(b, qty, bag_qty_rules)
            collector.append(res)
        return num_cur + num_cur * sum(collector)


if __name__ == "__main__":

    choice = input("run part 1 or 2, enter 1 or 2\n")
    if not choice in ("1", "2"):
        raise ValueError("please choose 1 or 2")

    file = "input_files/problem7.txt"

    if choice == "1":
        bag_rules = process_input(file)
        print(f"the answer to part 1 is {traverse_graph(bag_rules)}")

    elif choice == "2":
        bag_qty_rules = process_input_qty(file)
        total_bags = count_downstream_bags(target_bag, 1, bag_qty_rules)
        print(f"the answer to part 2 is {total_bags-1}")
