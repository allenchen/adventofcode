from collections import defaultdict

def part1():
    f = open("input1.txt")
    left_inputs = []
    right_inputs = []
    for l in f.readlines():
        if len(l) < 3:
            continue
        left, right = l.split("   ")
        left_inputs += [int(left)]
        right_inputs += [int(right)]
    
    sorted_left_inputs = sorted(left_inputs)
    sorted_right_inputs = sorted(right_inputs)

    total_diffs = []
    for (left,right) in zip(sorted_left_inputs, sorted_right_inputs):
        total_diffs += [abs(left - right)]
    
    return sum(total_diffs)

def part2():
    f = open("input1.txt")
    frequencies = defaultdict(int)
    left_list = []
    for l in f.readlines():
        if len(l) < 3:
            continue
        left, right = l.split("   ")
        left_list += [int(left)]
        frequencies[int(right)] += 1

    sim_scores = []
    for left in left_list:
        sim_scores += [left * frequencies[left]]
    
    return sum(sim_scores)

print(part2())