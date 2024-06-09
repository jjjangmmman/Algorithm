import sys
from collections import deque

def solution(line):
    q = deque()
    for ch in line:
        if ch=='(' or ch=='[':
            q.append(ch)
        if ch==')' or ch==']':
            if q:
                peek = q.pop()
                if (ch == ')' and peek!='(') or (ch == ']' and peek!='['):
                    return "no"
            else:
                return "no"
    return "yes" if not q else "no"

for line in sys.stdin.readlines()[:-1]:
    print(solution(line))