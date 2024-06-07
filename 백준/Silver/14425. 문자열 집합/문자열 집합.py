def solution(n,lines):
    D={}
    cnt=0
    for line in lines[:n]:
        D[line.strip()] = 1
    for line in lines[n:]:
        if line.strip() in D:
            cnt+=1
    return cnt
# i/o
import sys
tmp = sys.stdin.readlines()
n,m = map(int,tmp[0].strip().split())
lines = tmp[1:]
print(solution(n,lines))