from itertools import permutations #itertools패키지에서 permutations함수 가져옴
def solution(N,r):
    for p in permutations(range(1,N+1),r):
        print(*p)
N,r = map(int, input().split())
solution(N,r)
