import sys

A = [int(line) for line in sys.stdin.readlines()[1:]]
A.sort()
for a in A:
    print(a)