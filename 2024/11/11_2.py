from collections import defaultdict

memoized = defaultdict(int)

def check_memoized(stone: str, depth: int) -> int:
    return (stone, depth) in memoized.keys()

def get_memoized(stone: str, depth:int) -> int:
    return memoized[(stone, depth)]

def set_memoized(stone: str, depth:int, size: int) -> None:
    memoized[(stone, depth)] = size

def tick_stone(stone: str) -> list[str]:
    stone_int = int(stone)
    if stone_int == 0:
        return ["1"]
    elif len(stone) % 2 == 0:
        half_len = int(len(stone) / 2)
        first_half = str(int(stone[:half_len]))
        second_half = str(int(stone[half_len:]))
        return [first_half, second_half]
    else:
        return [str(stone_int * 2024)]

def tick_line_size(stones: list[str], depth: int) -> int:
    total_size = 0
    for s in stones:
        if check_memoized(s, depth):
            #print("Got memoized: {}, {}, {}", s, depth)
            total_size += get_memoized(s, depth)
        else:
            if depth == 1:
                total_size += len(tick_stone(s))
            else:
                delta_size = tick_line_size(tick_stone(s), depth - 1)
                set_memoized(s, depth, delta_size)
                total_size += delta_size
    return total_size

def main():
    line = ""
    f = open("input.txt", "r")
    for l in f.readlines():
        line += l
    line = line.split(" ")

    tls = tick_line_size(line, 75)
    
    print(tls)

main()