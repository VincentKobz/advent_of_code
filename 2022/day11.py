from dataclasses import dataclass
from functools import reduce
import math
import sys
import re
import heapq

@dataclass
class Monkey():
    """
    Monkey class
    """
    item_list: list
    operator: str
    arg_1: str
    arg_2: str
    div_nb: int
    true_monkey: int
    false_monkey:int

    def calculate_worry(self, item_value):
        arg_1, arg_2 = self.arg_1, self.arg_2
        arg_1 = int(arg_1) if arg_1 != "old" else int(item_value)
        arg_2 = int(arg_2) if arg_2 != "old" else int(item_value)

        if self.operator == '+':
            return arg_1 + arg_2
        else:
            return arg_1 * arg_2

def build_monkeys(stdin):
    """
    Parse and build monkeys list
    """
    monkeys = []
    for monkey in stdin:
        items = re.findall(r'\d+', monkey[1])
        arg_1, operator, arg_2 = monkey[2].split()[3], monkey[2].split()[4], monkey[2].split()[5]
        div_nb = monkey[3].split()[3]
        true_monkey = monkey[4].split()[5]
        false_monkey = monkey[5].split()[5]

        monkeys.append(Monkey(items, operator, arg_1, arg_2, int(div_nb), int(true_monkey), int(false_monkey)))

    return monkeys

def part_1(stdin):
    """
    Part 1
    """
    monkeys = build_monkeys(stdin)
    count = [0 for _ in range(len(monkeys))]

    for _ in range(20):
        for monkey in monkeys:
            for item in monkey.item_list:
                count[monkeys.index(monkey)] += 1
                new_item = monkey.calculate_worry(item)
                new_item = math.floor(new_item / 3)
                if new_item % monkey.div_nb == 0:
                    monkeys[monkey.true_monkey].item_list.append(new_item)
                else:
                    monkeys[monkey.false_monkey].item_list.append(new_item)
            monkey.item_list = []

    return reduce(lambda x, y: x * y, heapq.nlargest(2, count))

def part_2(stdin):
    """
    Part 2
    """
    monkeys = build_monkeys(stdin)
    count = [0 for _ in range(len(monkeys))]

    modulo = 1
    for monkey in monkeys:
        modulo *= monkey.div_nb

    for _ in range(10000):
        for monkey in monkeys:
            for item in monkey.item_list:
                count[monkeys.index(monkey)] += 1
                new_item = monkey.calculate_worry(item)
                new_item = new_item % modulo
                if new_item % monkey.div_nb == 0:
                    monkeys[monkey.true_monkey].item_list.append(new_item)
                else:
                    monkeys[monkey.false_monkey].item_list.append(new_item)
            monkey.item_list = []

    return reduce(lambda x, y: x * y, heapq.nlargest(2, count))


if __name__ == "__main__":
    res = sys.stdin.readlines()
    input, tmp = [], []

    for line in res:
        if line == '\n':
            input.append(tmp)
            tmp = []
        else:
            tmp.append(line.strip())
    input.append(tmp)
    
    print("Part_1 :", part_1(input))
    print("Part_2 :", part_2(input))
