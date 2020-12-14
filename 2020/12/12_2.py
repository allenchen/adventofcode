import math
def run(instructions):
    x, y = 0,0
    w_x, w_y = 10, 1
    dvecs = {
        'N': (0, 1),
        'S': (0, -1),
        'E': (1, 0),
        'W': (-1, 0)
    }
    for l in instructions.splitlines():
        instr_type = l[0]
        value = int(l[1:])
        if instr_type in ['L', 'R']:
            dx, dy = (w_x-x, w_y - y)
            if instr_type == 'R':
                value *= -1
            rvalue = math.radians(value)
            ndx = round((dx * math.cos(rvalue)) - (dy * math.sin(rvalue)))
            ndy = round((dx * math.sin(rvalue)) + (dy * math.cos(rvalue)))
            w_x, w_y = (x+ndx, y+ndy)
        elif instr_type in ['N', 'S', 'E', 'W']:
            w_x, w_y = (w_x + (dvecs[instr_type][0] * value), w_y + (dvecs[instr_type][1] * value))
        elif instr_type == 'F':
            dx, dy = (w_x - x, w_y - y)
            x, y = (x + (dx * value), y + (dy * value))
            w_x, w_y = (w_x + (dx * value), w_y + (dy * value))
    return (abs(x) + abs(y))

f = open("12.txt", "r")
print run(f.read())
