def add(t, x, y):
    return (t[0]+x, t[1]+y)

def invalid_pos(sand_pos, rock_locs, line_y):
    return sand_pos in rock_locs or sand_pos[1] == line_y

def solve(rock_locs, use_line):
    sand_start = (500, 0)
    max_y = max([ coord[1] for coord in rock_locs ])

    line_y = 2 + max_y
    if use_line:
        max_y = line_y
    count = 0
    sand_pos = sand_start
    while sand_pos[1] <= max_y:
        original = sand_pos
        sand_pos = add(sand_pos, 0, 1)
        if invalid_pos(sand_pos, rock_locs, line_y):
            sand_pos = add(sand_pos, -1, 0)
        if invalid_pos(sand_pos, rock_locs, line_y):
            sand_pos = add(sand_pos, 2, 0)
        if invalid_pos(sand_pos, rock_locs, line_y):
            rock_locs.add(original)
            sand_pos = sand_start
            count += 1
            if original == sand_start:
                break

    print(count)

if __name__ == "__main__":
    with open('example.txt') as f:
        lines = [ [ tuple([ int(x) for x in coord.split(',') ]) for coord in l.strip().split(" -> ")  ] for l in f.readlines() ]

        # Create set of rock locations
        rock_locs = set()
        for l in lines:
            for i in range(len(l)-1):
                from_coord = l[i]
                to_coord = l[i+1]
                idx = 0 if (from_coord[0] - to_coord[0]) != 0 else 1
                other = abs(idx - 1)
                range_num = to_coord[idx] - from_coord[idx]
                range_step = range_num // abs(range_num)
                range_num += range_step  
                for v in range(0, range_num, range_step):      
                    new_coord = ( from_coord[idx] + v, from_coord[other] )
                    rock_locs.add((new_coord[idx], new_coord[other]))

        # Part 1
        solve(rock_locs.copy(), False)

        # Part 2
        solve(rock_locs, True)