import re
from dataclasses import dataclass

@dataclass
class DirContents:
    size: int
    parent: str

def sum_sizes(directory_map, start_dir):
    dir = directory_map[start_dir]
    size = dir.size
    while dir.parent:
        dir = directory_map[dir.parent]
        dir.size += size 

if __name__ == "__main__":
    with open('input.txt') as f:
        lines = [ x.strip() for x in f.readlines() ]
        
        cd_pattern = r'^\$ cd (.+)$'
        dir_pattern = r'^dir (.+)$'
        file_pattern = r'^(\d+) .+$'

        directory_map = {}
        cd_search = True
        up_dir = ".."
        current_dir = ''

        i = 0
        while i < len(lines):
            l = lines[i]
            if cd_search: # cd into a directory
                match = re.search(cd_pattern, l)
                dir = match.group(1)
                if dir == up_dir:
                    current_dir = directory_map[current_dir].parent
                    i += 1

                else:
                    full_path = '/'.join([x for x in [current_dir, dir] if x])
                    directory_map[full_path] = DirContents(0, current_dir)
                    current_dir = full_path
                    cd_search = False
                    i += 2

            else: # find all dirs and files in this directory
                dir_match = re.search(dir_pattern, l)
                if file_match := re.search(file_pattern, l):
                    directory_map[current_dir].size += int(file_match.group(1))

                if dir_match or file_match:
                    i += 1
                else:
                    # add size to parent directories
                    sum_sizes(directory_map, current_dir)

                    # indicate we're now searching for cd
                    cd_search = True

        # sum for the final directory
        sum_sizes(directory_map, current_dir)
        
        # part 1
        max = 100000
        print(sum(filter(lambda y: y <= max,[ x.size for x in directory_map.values() ])))    

        # part 2
        required_space = 30000000 - (70000000 - directory_map["/"].size)
        print(min(filter(lambda y: y >= required_space,[ x.size for x in directory_map.values() ])))