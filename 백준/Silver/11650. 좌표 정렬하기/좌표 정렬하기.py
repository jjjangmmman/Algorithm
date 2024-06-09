import sys

a = [list(map(int,line.split())) for line in sys.stdin.readlines()[1:]]
a.sort(key=lambda x:(x[0],x[1]))
for rs in a:
    print(rs[0], rs[1])