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

def part2():
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

    swapped_updates = []
    for update in updates:
        updated = False
        for i_before, _ in enumerate(update):
            for i_after, _ in enumerate(update[(i_before+1):]):
                # main difference is to actually perform the swap if they aren't following the rules
                
                before = update[i_before]
                after = update[i_before + i_after + 1]
                if not follows_rules(before, after, rules_dag):
                    print("Performing swap: " + str(update[i_before]) + ", " + str(update[i_before + i_after + 1]) + " // " + str(after) + ", " + str(before))
                    update[i_before], update[i_before + i_after + 1] = after, before
                    print(update)
                    updated = True
        if updated:
            swapped_updates += [update]
    print(swapped_updates)
    middle_values = [update[len(update) // 2] for update in swapped_updates]

    return sum(middle_values)
                    

print(part2())