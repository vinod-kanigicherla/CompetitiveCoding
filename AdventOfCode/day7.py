import sys

class Node:
    def __init__(self, name, parent, size=None):
        self.name = name
        self.parent = parent
        self.size = size
        self.children = {}  # key=name, value=Node object

temp = [line.strip() for line in sys.stdin]

root = Node("/", None)
cwd = root
for l in temp:
    line = l.split(" ")
    if line[0] == "$":
        if line[1] == "cd":
            if line[2] == ".." and cwd.parent is not None:
                cwd = cwd.parent
            else:
                if line[2] in cwd.children:
                    cwd = cwd.children[line[2]]
        elif line[1] == "ls":
            pass
    else:
        if line[0] == "dir":
            # for dirs
            d = Node(line[1], cwd)
            cwd.children[line[1]] = d
        else:
            # for files
            f = Node(line[1], cwd, int(line[0]))
            cwd.children[line[1]] = f

total_sizes = []
def total_size(node):
    if node.size is not None:
        # node is a file
        return node.size
    else:
        # node is a folder
        ts = sum([total_size(c) for c in node.children.values()])
        total_sizes.append(ts)
        return ts


total_size(root)

print(sum([ts for ts in total_sizes if ts <= 100_000]))

print(total_sizes)

SPACE_NEEDED = max(total_sizes) - 40000000

print(min([ts for ts in total_sizes if ts >= SPACE_NEEDED]))