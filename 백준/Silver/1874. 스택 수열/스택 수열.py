import sys
from collections import deque

info = deque(int(line) for line in sys.stdin.readlines())
N = info.popleft()

A = deque(range(1,N+1))
stack = []
operations = []

for i in info:
    while A and (not stack or stack[-1] < i):
        stack.append(A.popleft())
        operations.append("+")
    if stack and stack[-1] == i:
        stack.pop()
        operations.append("-")
    elif stack and stack[-1] > i:
        print("NO")
        break
else:
    print("\n".join(operations))