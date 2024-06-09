import sys
from collections import deque

q = deque()
for line in sys.stdin.readlines()[1:]:
    if "push" in line:
        q.append(int(line.split()[1]))
    if "pop" in line:
        print(q.popleft() if q else -1)
    if "size" in line:
        print(len(q))
    if "empty" in line:
        print(0 if q else 1)
    if "front" in line:
        print(q[0] if q else -1)
    if "back" in line:
        print(q[-1] if q else -1)