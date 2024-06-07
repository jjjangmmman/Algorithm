def solution(n,lines):
    nSet = set(lines[:n])
    ret = [key.rstrip() for key in lines[n:] if key in nSet]
    ret.sort()
    print(len(ret))
    print(*ret,sep="\n")
# i/o
import sys
tmp = sys.stdin.readlines()
n,m = map(int,tmp[0].strip().split())
lines = tmp[1:]
solution(n,lines)