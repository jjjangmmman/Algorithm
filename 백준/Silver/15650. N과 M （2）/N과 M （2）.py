from itertools import combinations 
def solution(N,r):
    for p in combinations(range(1,N+1),r):
        print(*p)
N,r = map(int, input().split())
solution(N,r)