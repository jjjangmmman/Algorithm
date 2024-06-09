import sys
for a in sorted(int(line) for line in sys.stdin.readlines()[1:]):
    print(a)