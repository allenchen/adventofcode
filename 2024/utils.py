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
                    self.trailheads += [(x,y))]
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