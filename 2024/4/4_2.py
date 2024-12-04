def search(matrix: list[list[str]]):
    TARGET_WORD = "XMAS"

    height = len(matrix)
    width = len(matrix[0])

    def in_bounds(x, y):
        return (x >= 0 and x < width) and (y >= 0 and y < height)

    def count_crosses(x, y):
        # Count crosses with the center at (x,y)

        n_to_s = [(x-1, y-1), (x,y), (x+1, y+1)]
        s_to_n = [(x-1, y+1), (x,y), (x+1, y-1)]

        if all([in_bounds(x,y) for (x,y) in n_to_s + s_to_n]):
            n_to_s_word = ""
            s_to_n_word = ""
            for (x,y) in n_to_s:
                n_to_s_word += matrix[x][y]
            for (x,y) in s_to_n:
                s_to_n_word += matrix[x][y]
            
            if (n_to_s_word in ("MAS", "SAM") and (s_to_n_word in ("MAS", "SAM"))):
                return 1
            else:
                return 0
        else:
            return 0

    total_crosses = 0
    for y, l in enumerate(matrix):
        for x, _ in enumerate(l):
            # is there a cross centered at (x,y)
            total_crosses += count_crosses(x,y)
    
    return total_crosses

def part2():
    f = open("input1.txt")
    matrix = []
    for l in f.readlines():
        l = filter(lambda x: x.isalpha(), l)
        matrix += [list(l)]
    return search(matrix)

print(part2())