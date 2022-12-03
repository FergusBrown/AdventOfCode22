def intify(char):
    base = ord(char)+1
    return base-ord('a') if char.islower() else base-ord('A')+26

def part1():
    with open('input.txt') as f:
        rucksack_vals = [ intify(list(set(x[:len(x)//2]).intersection(set(x[len(x)//2:])))[0]) for x in f.readlines() ] 

        print(sum(rucksack_vals))

def part2():
    with open('input.txt') as f:
        line_sets = [ set(x.strip()) for x in f.readlines()]
        step_size=3
        badges = [ intify(list(set.intersection(*line_sets[i:i+step_size]))[0]) for i in range(0,len(line_sets),step_size) ]

        print(sum(badges))

if __name__ == "__main__":
    part1()
    part2()