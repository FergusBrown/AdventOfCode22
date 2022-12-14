import re
import operator
import math
import copy
from dataclasses import dataclass

@dataclass
class Monkey:
    items : list[str]
    op : operator
    other : str
    test : int
    throw : list[int]
    inspected = 0

def watch_monkeys(monkeys, num_rounds):
    mod_num = math.prod([t.test for t in monkeys])

    for _ in range(num_rounds):
        for m in monkeys:
            for _ in range(len(m.items)):
                item = m.items.pop(0)
                other = m.other
                if other == "old":
                    other = item
                item = m.op(item, int(other))
                item = item // 3 if num_rounds == 20 else item % mod_num
                next_monkey = m.throw[int(item % m.test == 0)]

                monkeys[next_monkey].items.append(item)
                m.inspected += 1

    inspected_list = sorted([ m.inspected for m in monkeys ])
    print(inspected_list[-1] * inspected_list[-2])

if __name__ == "__main__":
    with open('input.txt') as f:
        monkey_strings = f.read().strip().split("\n\n")
        items_pattern = r'Starting items: (.+)'
        operations_pattern = r'.*([+*]) (.+)'
        test_pattern = r'Test:.* (\d+)'
        true_pattern = r'true.* (\d+)'
        false_pattern = r'false.* (\d+)'

        monkeys = []
        for m in monkey_strings:
            items = [ int(x) for x in re.search(items_pattern, m).group(1).split(',') ]
            op_match = re.search(operations_pattern, m)
            other = op_match.group(2)
            op = (operator.add if op_match.group(1) == '+' else operator.mul)
            test = int(re.search(test_pattern, m).group(1))
            true = int(re.search(true_pattern, m).group(1))
            false = int(re.search(false_pattern, m).group(1))

            monkeys.append(Monkey(items, op, other, test, [false, true]))

        # Part 1
        watch_monkeys(copy.deepcopy(monkeys), 20)

        #Part 2
        watch_monkeys(monkeys, 10000)