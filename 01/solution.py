def solution():
    with open('input.txt') as f:
        elf_totals = sorted([ sum([ int(y) for y in x.split() ]) for x in f.read().split("\n\n") ])

        # Part 1
        print(elf_totals[-1])

        # Part 2
        print(sum(elf_totals[-3:]))

if __name__ == "__main__":
    solution()