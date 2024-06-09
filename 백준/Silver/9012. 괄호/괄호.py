import sys
from collections import deque

def VPS(line):
    s = deque()
    for ch in line:
        if ch=="(":
            s.append(ch)
        if ch==")":
            if s:
                s.pop()
            else:
                return "NO"
    if s:
        return "NO"
    else:
        return "YES"
        
for line in sys.stdin.readlines()[1:]:
    print(VPS(line))