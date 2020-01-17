import numpy as np
from pprint import pprint


def load_grid(test_string):
    lines = test_string.split("\n")[1:]
    shape = lines[0].split()

    shape = list(map(int, shape))

    grid = lines[1:]

    for i, row in enumerate(grid):
        grid[i] = "[" + row.replace(".", "False, ").replace("*", "True, ") + "]"
        grid[i] = eval(grid[i])
    grid = np.array(grid)

    return shape, grid


class Grid:
    def __init__(self, shape, grid):
        self.shape = shape
        self.grid = grid

    def next_gen(self):
        return self.count_live_neighbors((1, 4))

    def count_live_neighbors(self, coord):
        row, col = coord
        live_count = 0
        for y in range(-1, 2):
            for x in range(-1, 2):
                if self.validate_cords([row + y, col + x]) and not x == y == 0:
                    live_count += int(self.grid[row + y, col + x])

        return live_count

    def validate_cords(self, cord):
        y, x = cord
        shape_y, shape_x = self.shape
        if 0 <= y < shape_y and 0 <= x < shape_x:
            return True
        return False


if __name__ == "__main__":
    test_string = """
4 8
........
....*...
...**...
........"""

    shape, grid = load_grid(test_string)

    game = Grid(shape, grid)
    print(game.next_gen())
