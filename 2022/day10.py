import sys

def part_1(stdin):
    """
    Part 1
    """
    registry_x, nb_cycle= 1, 1
    save_cycle, res = [20, 60, 100, 140, 180, 220], 0

    for line in stdin:
        nb_loop = 1
        if line.split()[0] != "noop":
            nb_loop = 2

        for _ in range(nb_loop):
            if nb_cycle in save_cycle:
                res += nb_cycle * registry_x

            nb_cycle += 1

        registry_x += 0 if nb_loop != 2 else int(line.split()[1])

    return res

def part_2(stdin):
    """
    Part 2
    """
    save_cycle, res = [40, 80, 120, 160, 200, 240], []
    registry_x, nb_cycle, sprite_position, sprite = 1, 1, 1, ""

    for line in stdin:
        nb_loop = 1
        if line.split()[0] != "noop":
            nb_loop = 2

        for _ in range(nb_loop):
            if (nb_cycle % 40) >= sprite_position and (nb_cycle % 40) <= sprite_position + 2:
                sprite += '#'
            else:
                sprite += '.'

            if nb_cycle in save_cycle:
                res.append(sprite)
                sprite = ""

            nb_cycle += 1

        registry_x += 0 if nb_loop != 2 else int(line.split()[1])
        sprite_position = registry_x

    return res

if __name__ == "__main__":
    res = sys.stdin.readlines()
    print("Part_1 :", part_1(res))
    print("Part_2 :")
    for i in part_2(res):
        print(i)
