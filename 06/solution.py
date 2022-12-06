def solve(input, step):
    for i in range(len(input)):
        end_idx = i+step
        if (len(set(input[i:end_idx])) == step):
            return end_idx
    
    return -1

if __name__ == "__main__":
    with open('input.txt') as f:
        input = f.read().strip()

        # Part 1
        print(solve(input, 4))

        # Part 2
        print(solve(input, 14))