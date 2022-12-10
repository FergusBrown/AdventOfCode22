from dataclasses import dataclass

@dataclass(frozen=True)
class Pos:
    x : int
    y : int

    def __add__(self, other):
        return Pos(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Pos(self.x - other.x, self.y - other.y)

def parse_pair(line):
    s = line.split()
    return (s[0], int(s[1]))

def in_range(a, b):
    dist = a - b
    return abs(dist.x) <= 1 and abs(dist.y) <= 1

def get_dir(c):
    if c == 'R':
        return Pos(1, 0)
    elif c == 'L':
        return Pos(-1, 0)
    elif c == 'U':
        return Pos(0, 1)
    elif c == 'D':
        return Pos(0, -1)
    else:
        raise

def solve(pairs, length):
    start = Pos(0, 0)
    rope = [ start ] * length

    visited = set([ start ])

    for p in pairs:
        start_dir = get_dir(p[0])
        for i in range(p[1]):
            rope[0] += start_dir
            dir = start_dir
            for j in range(1, length):
                if not in_range(rope[j], rope[j-1]):
                    dir = rope[j-1] - rope[j]
                    dir = Pos(int(dir.x/2), int(dir.y/2))
                    rope[j] = rope[j-1] - dir
                else:
                    break
            visited.add(rope[length-1])

    print(len(visited))

if __name__ == "__main__":
    with open('input.txt') as f:
        lines = [ l for l in f.read().strip().split('\n') ]
        pairs = [ parse_pair(l.strip()) for l in lines ]

        # Part 1
        solve(pairs, 2)

        # Part 2
        solve(pairs, 10)