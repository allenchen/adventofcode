ACCEPTABLE_CHARACTERS = "^>v<.#"
GUARD = "^"
EMPTY = "."
OBSTACLE = "#"
N_GUARD = "^"
S_GUARD = "v"
E_GUARD = ">"
W_GUARD = "<"

from copy import deepcopy

def is_guard(o):
    return o == "^" or o == ">" or o == "v" or o == "<"

def get_guard_vector(o):
    if o == "^":
        return (0, -1)
    elif o == ">":
        return (1, 0)
    elif o == "v":
        return (0,1)
    elif o == "<":
        return (-1, 0)
    return None

class Board():
    def __init__(self, board: list[list[str]]):
        self.guard_position = None
        for y, l in enumerate(board):
            for x, o in enumerate(l):
                if is_guard(o):
                    self.guard_position = (x,y)
        self.height = len(board)
        self.width = len(board[0])
        self.board = board
        self.visited_guard_positions = set[tuple[int, int]]()
        self.visited_guard_positions.add(self.guard_position)

    def get(self, position):
        x, y = position
        return self.board[y][x]
    
    def set(self, position, value):
        x, y = position
        self.board[y][x] = value
        return True

    def make_move(self, old_position: tuple[int, int], new_position: tuple[int, int]):
        old_value = self.get(old_position)
        new_value = self.get(new_position)

        self.set(old_position, new_value)
        self.set(new_position, old_value)

        return True
    
    def turn_guard(self):
        guard = self.get(self.guard_position)

        if guard == N_GUARD:
            self.set(self.guard_position, E_GUARD)
        elif guard == E_GUARD:
            self.set(self.guard_position, S_GUARD)
        elif guard == S_GUARD:
            self.set(self.guard_position, W_GUARD)
        elif guard == W_GUARD:
            self.set(self.guard_position, N_GUARD)

        return None

    def in_bounds(self, position: tuple[int, int]):
        x,y = position
        return x >= 0 and x < self.width and y >= 0 and y < self.height
    
    def is_obstacle(self, position: tuple[int, int]):
        return self.get(position) == OBSTACLE
    
    def move_guard(self):
        # returns a new board state
        guard_vector = get_guard_vector(self.get(self.guard_position))
        print(guard_vector)
        print(self.guard_position)
        new_guard_position = (self.guard_position[0] + guard_vector[0], self.guard_position[1] + guard_vector[1])

        if not self.in_bounds(new_guard_position):
            # Terminal state!
            self.set(self.guard_position, EMPTY)
            self.guard_position = None
        elif self.is_obstacle(new_guard_position):
            # turn 90 degrees
            self.turn_guard()
        elif self.in_bounds(new_guard_position) and not self.is_obstacle(new_guard_position):
            # move the guard
            self.make_move(self.guard_position, new_guard_position)
            self.guard_position = new_guard_position
            self.visited_guard_positions.add(new_guard_position)
            

    def tick(self):
        # define where the guard is going to move to
        if self.guard_position == None:
            return True
        else:
            self.move_guard()
            return False

def part1():
    f = open("input1.txt")
    board = []
    for l in f.readlines():
        l = filter(lambda c: c in ACCEPTABLE_CHARACTERS, l)
        board += [list(l)]
    print(board)

    b = Board(board)

    while not b.tick():
        pass

    return b.visited_guard_positions

print(len(part1()))