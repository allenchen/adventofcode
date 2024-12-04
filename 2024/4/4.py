def search(matrix: list[list[str]]):
    TARGET_WORD = "XMAS"

    height = len(matrix)
    width = len(matrix[0])

    def in_bounds(x, y):
        return (x >= 0 and x < width) and (y >= 0 and y < height)

    def count_lines(x, y):
        # Count lines originating from (x, y)
        # {Horizontal, Vertical, Diagonal} x {Forwards, Backwards}

        originating_lines = 0

        horizontal_forwards = [(x,y), (x+1, y), (x+2, y), (x+3, y)]
        horizontal_backwards = [(x,y), (x-1, y), (x-2, y), (x-3, y)]
        vertical_forwards = [(x,y), (x, y+1), (x, y+2), (x, y+3)]
        vertical_backwards = [(x,y), (x, y-1), (x, y-2), (x, y-3)]
        diagonal_se = [(x, y), (x+1, y+1), (x+2, y+2), (x+3, y+3)]
        diagonal_sw = [(x, y), (x-1, y-1), (x-2, y-2), (x-3, y-3)]
        diagonal_ne = [(x, y), (x+1, y-1), (x+2, y-2), (x+3, y-3)]
        diagonal_nw = [(x, y), (x-1, y+1), (x-2, y+2), (x-3, y+3)]

        combinations = [
            horizontal_forwards,
            horizontal_backwards,
            vertical_forwards,
            vertical_backwards,
            diagonal_ne,
            diagonal_nw,
            diagonal_sw,
            diagonal_se
        ]

        for combination in combinations:
            if all([in_bounds(x,y) for (x,y) in combination]):
                word = ""
                for (x,y) in combination:
                    word += matrix[x][y]
                if word == TARGET_WORD:
                    originating_lines +=1
        
        return originating_lines

    total_lines = 0
    for y, l in enumerate(matrix):
        for x, _ in enumerate(l):
            print("Searching in: (" + str(x) + "," + str(y) + ")")
            total_lines += count_lines(x,y)
    
    return total_lines

def part1():
    f = open("input1.txt")
    matrix = []
    for l in f.readlines():
        l = filter(lambda x: x.isalpha(), l)
        matrix += [list(l)]
    return search(matrix)

print(part1())