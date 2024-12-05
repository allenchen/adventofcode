from collections import defaultdict

def create_rules_dag(rules: list[(int,int)]):
    dag = defaultdict(list[int])
    for (before, after) in rules:
        dag[before] += [after]
    return dag

def follows_rules(before, after, rules):
    after_nodes = rules[after]
    if before in after_nodes:
        return False
    return True


def part1():
    # create a dag of the page ordering rules (hopefully it's a dag, otherwise the rules would be invalid)
    f = open("input1.txt")
    rules = []
    updates = []

    section = 0
    for l in f.readlines():
        if len(l) <= 3:
            section = 1
            continue
        if section == 0:
            rule = [int(i) for i in l.split("|")]
            rules += [(rule[0], rule[1])]
        elif section == 1:
            updates += [[int(i) for i in l.split(",")]]

    rules_dag = create_rules_dag(rules)

    valid_updates = []
    for update in updates:
        update_results = []
        for i, before in enumerate(update):
            for after in update[i:]:
                update_results += [follows_rules(before, after, rules_dag)]
        if all(update_results):
            valid_updates += [update]

    middle_values = [update[len(update) // 2] for update in valid_updates]

    return sum(middle_values)
                    

print(part1())