if __name__ == "__main__":
    with open('input.txt') as f:
        lines = [ l.strip().split() for l in f.read().strip().split('\n') ]

        # find the cycles we need to add
        add_map = {}
        cycle_count = 1
        for l in lines:
            cycle_count += 1
            if l[0] == "addx":
                cycle_count += 1
                add_map[cycle_count] = int(l[1])
        
        # execute the cycles
        x = 1
        step = 40 
        check_range = range(20, 221, step)
        signal_strength = 0
        pixels = ""
        for cycle in range(1, 241):
            x += add_map.get(cycle, 0)

            # Part 1
            if cycle in check_range:
                signal_strength += cycle * x

            # Part 2
            crt_idx = (cycle - 1) % step
            sprite_range = range(x-1, x+2)
            if crt_idx in sprite_range:
                pixels += '#'
            else:
                pixels += '.'

        # Part 1
        print(signal_strength)

        # Part 2
        for i in range(0, 240, step):
            print(pixels[i:i+step])