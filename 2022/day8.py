import sys
import numpy as np

def part_1(stdin):
    """
    Part 1
    """
    matrix = np.array([[int(elt) for elt in line] for line in stdin])
    visible_matrix = np.array([[False for _ in line] for line in stdin])

    for i in range(len(matrix)):
        for row in range(len(matrix)):

            if i == 0 or max(matrix[row][:i]) < matrix[row][i]:
                visible_matrix[row][i] = True

            elif i == len(matrix) - 1 or max(matrix[row][i+1:]) < matrix[row][i]:
                visible_matrix[row][i] = True

            elif row == 0 or max(matrix[:row,i]) < matrix[row][i]:
                visible_matrix[row][i] = True

            elif row == len(matrix) - 1 or max(matrix[(row+1):,i]) < matrix[row][i]:
                visible_matrix[row][i] = True

    return visible_matrix.sum()

def part_2(stdin):
    """
    Part 2
    """
    def get_view_distance(list, value):
        """
        Returns the view distance with a given list and a base value
        """
        i = 1
        if list[0] >= value:
            return i

        while i < len(list) and (list[i - 1] < list[i] or list[i - 1] < value):
            i += 1
        return i

    matrix = np.array([[int(elt) for elt in line] for line in stdin])
    visible_matrix = np.array([[1 for _ in line] for line in stdin])

    for i in range(len(matrix)):
        for row in range(len(matrix)):
            if i == 0 or row == 0 or i == len(matrix) - 1 or row == len(matrix) - 1:
                visible_matrix[row][i] = 0
                continue
            
            value = matrix[row][i]

            # left
            visible_matrix[row][i] *= get_view_distance(matrix[row][:i][::-1], value)
            # right
            visible_matrix[row][i] *= get_view_distance(matrix[row][i+1:], value)
            # up
            visible_matrix[row][i] *= get_view_distance(matrix[:row,i][::-1], value)
            # down
            visible_matrix[row][i] *= get_view_distance(matrix[(row + 1):,i], value)

    return visible_matrix.max()

if __name__ == "__main__":
    res = sys.argv[1]
    stdin = res.split('\n')
    print(part_1(stdin))
