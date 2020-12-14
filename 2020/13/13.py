import math

def run(instructions):
    lines = instructions.splitlines()
    my_departure = int(lines[0])
    buses = filter(lambda x: x != "x", (lines[1].strip().split(",")))
    print buses
    bus_map = {}
    
    for bus in buses:
        bus = int(bus)
        closest_departure = math.ceil(my_departure / float(bus))
        bus_map[bus] = closest_departure * bus - my_departure
    return min(bus_map.iteritems(), key=lambda x: x[1])


f = open("13.txt", "r")
result = run(f.read())
print result
print result[0] * result [1]
