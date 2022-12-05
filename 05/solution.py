import copy
import re

def part1(stacks, directions):
    for d in directions:
        for i in range(d[0]):
            from_stack = stacks[d[1]-1]
            to_stack = stacks[d[2]-1]
            to_stack.append(from_stack.pop())

    print(''.join([ x[-1] for x in stacks]))

def part2(stacks, directions):
    for d in directions:
        from_stack = stacks[d[1]-1]
        to_stack = stacks[d[2]-1]
        to_stack.extend(from_stack[-d[0]:])
        del from_stack[-d[0]:]

    print(''.join([ x[-1] for x in stacks]))

if __name__ == "__main__":
    with open('input.txt') as f:
        inputs = f.read().split("\n\n")
        positions_input = inputs[0].split('\n')
        positions_input.reverse()

        stacks = [ [] for _ in range(len(re.findall(r'\d', positions_input[0]))) ]

        for line in positions_input[1:]:
            for i in range(1, len(line), 4):
                if re.search(r'\S', line[i]):
                    stacks[(i - 1) // 4].append(line[i])

        directions_input = inputs[1].strip().split('\n')

        directions = [ [ int(y) for y in re.findall(r'\d+', x) ] for x in directions_input ]

        part1(copy.deepcopy(stacks),directions[:])

        part2(copy.deepcopy(stacks),directions[:])