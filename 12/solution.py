import queue
import sys

def get_neighbours(grid, width, height, idx):
    x = idx % width
    y = idx // width

    neighbours = []
    # up
    if y != 0:
        neighbours.append(idx - width)

    # down
    if y != (height - 1):
        neighbours.append(idx + width)

    # left
    if x != 0:
        neighbours.append(idx - 1)

    # right
    if x != (width-1):
        neighbours.append(idx + 1)

    # filter indices which we can travel to
    return [ x for x in neighbours if ord(grid[x]) <= ord(grid[idx]) + 1 ]

def shortest_path(grid, width, height, start_idx, end_idx):
        q = queue.PriorityQueue() # add data in pairs (priority, data)
        dist = {}
        dist[start_idx] = 0

        q.put((dist[start_idx], start_idx))

        while not q.empty():
            u = q.get()[1]
            for v in get_neighbours(grid, width, height, u):
                alt = dist[u] + 1
                if alt < dist.get(v, sys.maxsize):
                    dist[v] = alt
                    q.put((alt, v))

        return dist.get(end_idx, sys.maxsize)

if __name__ == "__main__":
    with open('example.txt') as f:
        lines = f.readlines()
        height = len(lines)
        width = len(lines[0].strip())
        grid = [ c for l in lines for c in l.strip() ]
        start_idx = grid.index('S')
        end_idx = grid.index('E')
        grid[start_idx] = 'a'
        grid[end_idx] = 'z'

        # Part 1
        print(shortest_path(grid, width, height, start_idx, end_idx))

        # Part 2
        print(min([ shortest_path(grid, width, height, x, end_idx) for x in [ i for i in range(len(grid)) if grid[i] == 'a' ] ]))