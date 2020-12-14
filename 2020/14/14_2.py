import re
from copy import deepcopy
mem_pattern = re.compile("mem\[([0-9]+)\] = ([0-9]+)")

def parse_instruction(line):
    if line.startswith("mask = "):
        return ("MASK", line[7:])
    elif line.startswith("mem["):
        return ("MEM", mem_pattern.findall(line)[0])
    else:
        return None

def replace_xs(s, replacement):
    s_cpy = deepcopy(s)
    r_cpy = deepcopy(replacement)
    while True:
        try:
            ind = s_cpy.index("X")
            s_cpy[ind] = r_cpy[0]
            r_cpy = r_cpy[1:]
        except Exception as e:
            return s_cpy
    
def apply_mask(value, mask):
    bv = '{0:036b}'.format(int(value))
    resulting_value = []
    xs = 0
    for v, m in zip(bv, mask):
        if m == "0":
            resulting_value += [v]
        elif m == "1":
            resulting_value += [m]
        else:
            resulting_value += ["X"]
            xs += 1

    tmpl = '{{0:0{}b}}'.format(xs)
    replacements = []
    for i in xrange(2**xs):
        replacements += [tmpl.format(i)]

    results = []
    for r in replacements:
        replaced = replace_xs(resulting_value, r)
        results += [replaced]

    final_result = map(lambda x: int(''.join(x), 2), results)
    return final_result
    
def run(f):
    current_mask = ""
    all_memory = {}
    for l in f.readlines():
        itype, values = parse_instruction(l)
        if itype == "MASK":
            current_mask = values
        elif itype == "MEM":
            mem_location = int(values[0])
            value = int(values[1])
            addresses = apply_mask(mem_location, current_mask)
            for addr in addresses:
                all_memory[addr] = value
    return sum(all_memory.values())

if __name__ == "__main__":
    f = open("14.txt", "r")
    print run(f)
