import sys
from dataclasses import dataclass

@dataclass
class Point():
    x: int = 0
    y: int = 0

    def move_point(self, move, moves):
        add_x, add_y = moves[move]
        self.x += add_x
        self.y += add_y

    def add_coords(self, coord):
        (x, y) = coord
        x = 1 if x > 1 else -1 if x < -1 else x
        y = 1 if y > 1 else -1 if y < -1 else y
        self.x += x
        self.y += y

    def tail_move(self, tail):
        x_diff, y_diff = abs(self.x - tail.x), abs(self.y - tail.y)

        x_sign = 1 if self.x - tail.x < 0 else -1
        y_sign = 1 if self.y - tail.y < 0 else -1

        if x_diff > 1 and y_diff == 0:
            return self.x - tail.x + x_sign, 0

        if y_diff > 1 and x_diff == 0:
            return 0, self.y - tail.y + y_sign

        if x_diff > 1:
            return self.x - tail.x + x_sign, self.y - tail.y
        elif y_diff > 1:
            return self.x - tail.x, self.y - tail.y + y_sign

        return 0, 0

def part_1(stdin):
    """
    Part 1
    """
    moves, uniq_coords = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}, {(0, 0)}
    head, tail = Point(), Point()

    for line in stdin:
        move, nb_move = line.split()[0], int(line.split()[1])

        for _ in range(nb_move):
            head.add_coords(moves[move])
            tail_x, tail_y = head.tail_move(tail)

            tail.add_coords((tail_x, tail_y))
            uniq_coords.add((tail.x, tail.y))

    return len(uniq_coords)

def part_2(stdin):
    """
    Part 2
    """
    moves, uniq_coords, old_pos = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}, {(0, 0)}, [Point() for _ in range(10)]

    for line in stdin:
        move, nb_move = line.split()[0], int(line.split()[1])

        for _ in range(nb_move):
                old_pos[0].add_coords(moves[move])

                for i in range(9):
                    tail_x, tail_y = old_pos[i].tail_move(old_pos[i + 1])
                    old_pos[i + 1].add_coords((tail_x, tail_y))

                uniq_coords.add((old_pos[9].x, old_pos[9].y))

    return len(uniq_coords)

if __name__ == "__main__":
    res = sys.stdin.readlines()
    print("Part 1:", part_1(res))
    print("Part 2:", part_2(res))
