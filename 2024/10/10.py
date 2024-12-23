def acceptable_char(c):
    return c in "0123456789" or c == "."

def is_traversable(c):
    return c in "0123456789"

def is_trailhead(c):
    return c == "0"

VECTOR_N = (0, -1)
VECTOR_E = (1, 0)
VECTOR_W = (-1, 0)
VECTOR_S = (0, 1)

DIRECTIONAL_VECTORS = (VECTOR_E, VECTOR_N, VECTOR_S, VECTOR_W)

def vec_add(a, b):
    return (a[0] + b[0], a[1] + b[1])

class Board():
    def __init__(self, board: list[list[str]]):
        self.board = board
        self.trailheads = []
        for y, l in enumerate(board):
            for x, o in enumerate(l):
                if is_trailhead(o):
                    self.trailheads += [(x,y)]
        self.height = len(board)
        self.width = len(board[0])
        self.board = board

    def get(self, position):
        x, y = position
        return self.board[y][x]
    
    def set(self, position, value):
        x, y = position
        self.board[y][x] = value
        return True

    def in_bounds(self, position: tuple[int, int]):
        x,y = position
        return x >= 0 and x < self.width and y >= 0 and y < self.height
    
    def neighbors(self, position):
        neighbors = []
        for vector in DIRECTIONAL_VECTORS:
            neighbor = vec_add(position, vector)
            if self.in_bounds(neighbor) and is_traversable(self.get(neighbor)):
                neighbors += [neighbor]

        return neighbors
    
    def find_valid_neighbors(self, position):
        position_value = self.get(position)
        desired_value = str(int(position_value) + 1)

        ns = self.neighbors(position)
        valid_neighbors = []
        for n in ns:
            if self.get(n) == desired_value:
                valid_neighbors += [n]

        return valid_neighbors
    
    def trailhead_score(self, trailhead):
        # bfs
        visit_queue = self.find_valid_neighbors(trailhead)

        score = set()
        while len(visit_queue) > 0:
            visit_node = visit_queue.pop()
            if self.get(visit_node) == "9":
                score.add(visit_node)

            visit_queue += self.find_valid_neighbors(visit_node)
        return len(score)
    
    def total_score(self):
        ts = 0
        for t in self.trailheads:
            score = self.trailhead_score(t)
            print(score)
            ts += score
        return ts
        

def part1():
    f = open("input1.txt")
    board = []
    for l in f.readlines():
        l = filter(lambda c: acceptable_char(c), l)
        board += [list(l)]
    map = Board(board)

    return map.total_score()

print(part1())