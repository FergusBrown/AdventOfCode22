import re
import functools

def strip_n_split(s):
    ret = []
    if m := re.search(r'^\[(.*)\]$', s):
        s = m.group(1)
        count = 0
        indices = [-1]
        for i in range(len(s)):
            if s[i] == '[':
                count+=1
            elif s[i] == ']':
                count-=1
            elif s[i] == ',' and count == 0:
                indices.append(i)

        split_string = [ s[i+1:j] for i,j in zip(indices,indices[1:] + [None]) ]
        ret = split_string
    else:
        ret = [s]

    return list(filter(None, ret))

def in_order(left, right):
    list_l = strip_n_split(left)
    list_r = strip_n_split(right)
    
    for l,r in zip(list_l,list_r):
        if l.isdigit() and r.isdigit():
            if l != r:
                return int(l) < int(r)

        elif (res:=in_order(l, r)) != None:
            return res

    if len(list_r) == len(list_l):
        return None
    else:
        return len(list_r) > len(list_l)

def part1(pairs):
    count = 0
    for i, p in enumerate(pairs):
        if in_order(p[0], p[1]):
            count += i+1

    print(count)

def part2(pairs):
    input = [ x for p in pairs for x in p ]
    divider_packets = [ "[[2]]", "[[6]]"]
    input += divider_packets

    input.sort(key=functools.cmp_to_key(lambda a,b: -1 if in_order(a,b) else 1))

    print((input.index(divider_packets[0])+1) * (input.index(divider_packets[1])+1))

if __name__ == "__main__":
    with open('example.txt') as f:
        pairs = [ x.split('\n') for x in f.read().strip().split('\n\n') ]

        part1(pairs)
        part2(pairs)