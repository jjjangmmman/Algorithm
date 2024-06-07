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

# idolphin씨의 코드
from sys import stdin
input = stdin.readline
N, M = map(int, input().split())
nSet = {input().rstrip() for _ in range(N)}
answer = 0
for _ in range(M):
    key = input().rstrip()
    if key in nSet:
        answer += 1
print(answer)
키값이 필요없을때는 딕셔너리를 쓰지않고 집합 컴프리헨션으로 간단하게 처리하는게 매우 인상적
