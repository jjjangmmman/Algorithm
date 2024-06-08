def solution(N):
    D = {}
    for _ in range(N):
        eng, __, minion = input().rstrip().split()
        D[eng] = minion
    for _ in range(int(input().rstrip())):
        input()
        ret = []
        for eng in input().rstrip().split():
            ret.append(D[eng])
        print(*ret)
    
# i/o
import sys
input = sys.stdin.readline
N = int(input().rstrip())
solution(N)