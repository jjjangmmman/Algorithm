import sys
from collections import deque

s = deque()
for line in sys.stdin.readlines()[1:]:
    if "push" in line:
        s.append(int(line.split()[1]))
    if "pop" in line:
        print(s.pop() if s else -1)
    if "size" in line:
        print(len(s))
    if "empty" in line:
        print(0 if s else 1)
    if "top" in line:
        print(s[-1] if s else -1)