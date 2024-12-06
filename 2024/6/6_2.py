ACCEPTABLE_CHARACTERS = "^>v<.#"
GUARD = "^"
EMPTY = "."
OBSTACLE = "#"
N_GUARD = "^"
S_GUARD = "v"
E_GUARD = ">"
W_GUARD = "<"

LOOP_DETECTED = "LOOP"
EXITED_PREMISES = "EXIT"
NON_TERMINAL = "NON_TERMINAL"

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
                    guard_direction = o
                    self.guard_position = (x,y)
        self.height = len(board)
        self.width = len(board[0])
        self.board = board
        self.visited_guard_positions = set[tuple[tuple[int, int], str]]()
        self.visited_guard_positions.add((self.guard_position, guard_direction))
        self.terminal_state = NON_TERMINAL

    def copy(self):
        new_board_raw = deepcopy(self.board)
        return Board(new_board_raw)

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
    
    def is_empty(self, position: tuple[int, int]):
        return self.get(position) == EMPTY
    
    def place_obstacle(self, position):
        x,y = position
        self.board[y][x] = OBSTACLE
        return True
    
    def move_guard(self):
        # returns a new board state
        guard = self.get(self.guard_position)
        guard_vector = get_guard_vector(self.get(self.guard_position))
        #print(guard_vector)
        #print(self.guard_position)
        new_guard_position = (self.guard_position[0] + guard_vector[0], self.guard_position[1] + guard_vector[1])

        if (new_guard_position, guard) in self.visited_guard_positions:
            self.terminal_state = LOOP_DETECTED
        elif not self.in_bounds(new_guard_position):
            # Terminal state!
            self.set(self.guard_position, EMPTY)
            self.guard_position = None
            self.terminal_state = EXITED_PREMISES
        elif self.is_obstacle(new_guard_position):
            # turn 90 degrees
            self.turn_guard()
        elif self.in_bounds(new_guard_position) and not self.is_obstacle(new_guard_position):
            # move the guard
            self.make_move(self.guard_position, new_guard_position)
            self.guard_position = new_guard_position
            self.visited_guard_positions.add((new_guard_position, guard))
            
    def tick(self):
        # define where the guard is going to move to
        if self.terminal_state is not NON_TERMINAL:
            return True
        else:
            self.move_guard()
            return False

def part2():
    f = open("input1.txt")
    board = []
    for l in f.readlines():
        l = filter(lambda c: c in ACCEPTABLE_CHARACTERS, l)
        board += [list(l)]
    print(board)

    b = Board(board)

    valid_positions = 0

    for x in range(b.width):
        for y in range(b.height):
            position = (x,y)
            print(position)
            new_board = b.copy()
            if new_board.is_empty(position):
                new_board.place_obstacle(position)
                while not new_board.tick():
                    pass
                if new_board.terminal_state == LOOP_DETECTED:
                    valid_positions += 1

    return valid_positions

print(part2())