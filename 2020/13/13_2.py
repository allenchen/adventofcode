def find_next_time(starting_time, period, num, distance):
    st = starting_time
    while True:
        if (st + distance) % num == 0:
            return st
        st += period

def run(buses):
    buf = []
    last_result = 0
    for item in buses:
        if item is not "x":
            period = reduce(lambda x,y: int(x)*int(y), filter(lambda x: x is not "x", buf), 1) # multiply everything in buf
            last_result = find_next_time(last_result, period, int(item), len(buf))
        buf += [item]
    return last_result

if __name__ == "__main__":
    f = open("13_2.txt", "r")
    print run(f.read().splitlines()[1].split(","))
