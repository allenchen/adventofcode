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

def tick_line(stones: list[str]) -> list[str]:
    new_line = []
    for s in stones:
        t = tick_stone(s)
        
        new_line += t
    return new_line

def main():
    line = ""
    f = open("input.txt", "r")
    for l in f.readlines():
        line += l
    line = line.split(" ")
    
    for _ in range(25):
        line = tick_line(line)
    
    print(len(line))

main()