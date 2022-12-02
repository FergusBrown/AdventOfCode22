def part1():
    with open('input.txt') as f:
        rps_pairs = [ (z[0]-ord('A'),z[1]-ord('X')) for z in [ tuple([ord(y.strip()) for y in x.split()]) for x in f.readlines() ] ]

        total = 0
        for elf, me in rps_pairs:
            total += me + 1
            win_val = (elf + 1) % 3
            if elf == me:
                total += 3
            elif me == win_val:
                total += 6

        print(total)

def part2():
    with open('input.txt') as f:
        rps_pairs = [ (z[0]-ord('A'),z[1]-ord('X')) for z in [ tuple([ord(y.strip()) for y in x.split()]) for x in f.readlines() ] ]

        total = 0
        result_vals = [0, 3, 6]
        for elf, strat in rps_pairs:
            lose = (3 + elf - 1) % 3
            draw = elf
            win = (elf + 1) % 3
            strat_vals = [lose, draw, win]
            total += strat_vals[strat] + 1 + result_vals[strat]

        print(total)

if __name__ == "__main__":
    part1()
    part2()