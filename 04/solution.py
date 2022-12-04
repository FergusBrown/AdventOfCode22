def complete_overlap(a, b):
    return (a[0] <= b[0] and a[-1] >= b[-1]) or (b[0] <= a[0] and b[-1] >= a[-1])

def any_overlap(a, b):
    return bool(range(max(a[0], b[0]), min(a[-1], b[-1])+1))

def solution(lines):
    parsed_list = [ [ [ int(z) for z in y.split('-') ] for y in x.split(',') ] for x in lines ]

    # Part 1
    print(len(list(filter(lambda ranges: complete_overlap(ranges[0], ranges[1]), parsed_list))))

    #Part 2
    print(len(list(filter(lambda ranges: any_overlap(ranges[0], ranges[1]), parsed_list))))

if __name__ == "__main__":
    with open('input.txt') as f:
        lines = [ x.strip() for x in f.readlines() ]
        solution(lines)