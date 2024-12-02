def is_safe(level: list[int]):
    # all increasing or all decreasing
    # any two adjacent levels differ by at least one and at most 3

    print(level)
    sign = 0 # use sign-flip to determine increasing/decreasing
    for a, b in zip(level, level[1:]):
        expected_sign = 0
        diff = b-a

        print(diff)
        if (diff < 0):
            expected_sign = -1
        elif (diff > 0):
            expected_sign = 1
        else:
            return False
        
        if sign == 0:
            sign = expected_sign
        elif expected_sign != sign:
            return False
        
        if (abs(diff) < 1 or abs(diff) > 3):
            return False
    return True
    
def part1():
    f = open("input1.txt")
    safeties = []
    for l in f.readlines():
        if len(l) < 5:
            continue
        level = [int(x) for x in l.split(" ")]
        safeties += [is_safe(level)]
    
    print(safeties)
    return sum([1 for x in safeties if x])

def create_level_variations(level: list[int]):
    variations = []
    for i in range(len(level)):
        new_variation = level[:i] + level[(i+1):]
        variations += [new_variation]
    return variations

def part2():
    f = open("input1.txt")
    safeties = []
    for l in f.readlines():
        if len(l) < 5:
            continue
        level = [int(x) for x in l.split(" ")]

        variations = create_level_variations(level)
        safeties += [any([is_safe(variation) for variation in variations])]
    
    print(safeties)
    return sum([1 for x in safeties if x])

print(part2())