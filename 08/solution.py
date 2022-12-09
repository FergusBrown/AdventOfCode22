from dataclasses import dataclass

@dataclass
class Tree:
    visible: bool
    score: int

def evaluate_direction(numbers, i, stop, step) -> Tree:
    starting_height = numbers[i]
    r = range(i, stop, step)[1:]
    ret = Tree(True, 0)
    for j in r:
        ret.score += 1
        if numbers[j] >= starting_height:
            ret.visible = False
            break

    return ret

def evaluate_tree(numbers, i, width) -> Tree:
    x = i % width
    y = i // width
    max_idx = width - 1
    if x == 0 or y == 0 or x == max_idx or y == max_idx:
        return Tree(True, 0)
    else:
        right = evaluate_direction(numbers, i, (y + 1) * width, 1) 
        left = evaluate_direction(numbers, i, y * width - 1, -1) 
        up = evaluate_direction(numbers, i, len(numbers), width) 
        down = evaluate_direction(numbers, i, -1, -width)
        return Tree(left.visible or right.visible or up.visible or down.visible, left.score * right.score * up.score * down.score)

if __name__ == "__main__":
    with open('input.txt') as f:
        lines = f.readlines()
        width = len(lines)
        numbers = [ int(item) for sublist in lines for item in sublist.strip() ]

        visible_count = 0
        max_score = 0
        for i in range(width**2):
            result_tree = evaluate_tree(numbers, i, width)
            if result_tree.visible:
                visible_count += 1
                max_score = max(max_score, result_tree.score) 

        # Part 1
        print(visible_count)

        # Part 2
        print(max_score)