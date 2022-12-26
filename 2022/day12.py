import queue
import sys
import math

move = {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}

def find_coords(matrix, elt):
    """
    Find coords of start minimum path search
    """
    for index, row in enumerate(matrix):
        try:
            return (index, row.index(elt))
        except ValueError:
            continue

    return None

def get_height(elt):
    """
    Return weight of elt
    """
    if elt == 'S':
        return ord('a')

    if elt == 'E':
        return ord('z')

    return ord(elt)

def find_neighbour(x, y, matrix):
    """
    Return the neighbour near (x, y) vertex
    """
    current_elt = get_height(matrix[x][y])
    neighbour = []
    for elt in move:
        add_x, add_y =  move[elt]
        new_x, new_y = x + add_x, y + add_y

        if new_x < 0 or new_x >= len(matrix) or new_y < 0 or new_y >= len(matrix[0]):
            continue

        neighbour_elt = get_height(matrix[new_x][new_y])

        if current_elt + 1 >= neighbour_elt:
            neighbour.append((new_x, new_y))

    return neighbour

def get_min(distance, list):
    """
    Return the vertex with the minimum distance inside list
    """
    min = math.inf
    res = -1
    for i, (x, y) in enumerate(list):
        if distance[x][y] < min:
            min = distance[x][y]
            res = i

    return res

def dijkstra(matrix, src_x, src_y):
    distance, visited = [[math.inf for _ in range(len(matrix[0]))] for _ in range(len(matrix))], {}
    (dst_x, dst_y) = find_coords(matrix, "E")
    distance[src_x][src_y] = 0

    to_be_visited = []
    to_be_visited.append((src_x, src_y))

    while to_be_visited != []:
        x, y = to_be_visited.pop(get_min(distance, to_be_visited))
        if (x, y) in visited:
            continue

        visited[(x, y)] = True
        neighbour = find_neighbour(x, y, matrix)

        for (nei_x, nei_y) in neighbour:
            if distance[x][y] + 1 < distance[nei_x][nei_y]:
                distance[nei_x][nei_y] = distance[x][y] + 1
                to_be_visited.append((nei_x, nei_y))

    return distance, dst_x, dst_y

def part_1(stdin):
    """
    Part 1
    """
    matrix = [[elt for elt in line][:-1] for line in stdin]
    distance, dst_x, dst_y = dijkstra(matrix, *find_coords(matrix, "S"))
    return distance[dst_x][dst_y]

def part_2(stdin):
    """
    Part 2
    """
    matrix = [[elt for elt in line][:-1] for line in stdin]

    coords_a = []

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 'S' or matrix[row][col] == 'a':
                coords_a.append((row, col))

    res = []
    for (x, y) in coords_a:
        distance, dst_x, dst_y = dijkstra(matrix, x, y)
        res.append(distance[dst_x][dst_y])

    return min(res)


if __name__ == "__main__":
    res = sys.stdin.readlines()
    
    print("Part_1 :", part_1(res))
    print("Part_2 :", part_2(res))
