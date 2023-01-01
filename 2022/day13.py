import sys
import numpy as np
from functools import cmp_to_key

def refactor(stdin):
    """
    Refactor stdin input
    """
    res, tmp = [], []
    for line in stdin:
        if line == '\n':
            res.append(tmp)
            tmp = []
        else:
            tmp.append(line[:-1])

    res.append(tmp)
    return res

def is_right_order(packet_1, packet_2):
    """
    Check if packets are is the right order
    """
    index = 0

    while index < len(packet_1) and index < len(packet_2):
        elt_1, elt_2 = packet_1[index], packet_2[index]

        if type(elt_1) == int and type(elt_2) == int:
            if elt_1  > elt_2:
                return -1
            if elt_1 < elt_2:
                return 1

        elif type(elt_1) != int and type(elt_2) != int:
            tmp = is_right_order(elt_1, elt_2)
            if tmp != 0:
                return tmp

        elif type(elt_1) == int and type(elt_2) != int:
            tmp = is_right_order([elt_1], elt_2)
            if tmp != 0:
                return tmp

        elif type(elt_1) != int and type(elt_2) == int:
            tmp = is_right_order(elt_1, [elt_2])
            if tmp != 0:
                return tmp
        
        index += 1

    # left side out of range
    if index == len(packet_1) and index < len(packet_2):
        return 1

    # element are equal
    if len(packet_1) == len(packet_2):
        return 0

    # right side out of range
    return -1

def process(list):
    """
    Process all comparisons between pairs of packets
    """
    good_order_pair = []

    for index, pair in enumerate(list):
        if is_right_order(eval(pair[0]), eval(pair[1])) == 1:
            good_order_pair.append(index + 1)

    return good_order_pair

def part_1(stdin):
    """
    Part 1
    """
    res = process(refactor(stdin))
    res = np.array(res)

    return res.sum()

def part_2(stdin):
    """
    Part 2
    """
    dic = {}
    for index, line in enumerate(stdin):
        if line == '\n':
            continue

        dic[index] = eval(line)

    dic[index + 1] = eval('[[2]]')
    dic[index + 2] = eval('[[6]]')

    res = list(sorted(dic.values(), key=cmp_to_key(is_right_order), reverse=True))
    return (res.index([[6]]) + 1) * (res.index([[2]]) + 1)

if __name__ == "__main__":
    res = sys.stdin.readlines()
    
    print("Part_1 :", part_1(res))
    print("Part_2 :", part_2(res))
