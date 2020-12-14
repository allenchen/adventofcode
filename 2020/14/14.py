import re
mem_pattern = re.compile("mem\[([0-9]+)\] = ([0-9]+)")

def parse_instruction(line):
    if line.startswith("mask = "):
        return ("MASK", line[7:])
    elif line.startswith("mem["):
        return ("MEM", mem_pattern.findall(line)[0])
    else:
        print "Bad instruction"
        return None

def apply_mask(value, mask):
    print "applying mask"
    print value
    print mask
    bv = '{0:036b}'.format(int(value))
    print bv
    result = []
    for v, m in zip(bv, mask):
        if m == "X":
            result += [v]
        else:
            result += [m]
    result = int(''.join(result), 2)
    print result
    return result
    
def run(f):
    current_mask = ""
    all_memory = {}
    for l in f.readlines():
        itype, values = parse_instruction(l)
        print values
        if itype == "MASK":
            current_mask = values
        elif itype == "MEM":
            mem_location = int(values[0])
            value = int(values[1])
            result = apply_mask(value, current_mask)
            all_memory[int(mem_location)] = result
    print "exiting"
    return sum(all_memory.values())

if __name__ == "__main__":
    f = open("14.txt", "r")
    print run(f)
