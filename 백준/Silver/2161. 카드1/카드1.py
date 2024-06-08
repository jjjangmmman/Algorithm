from collections import deque

def solution(N):
    ret=[]
    q = deque(range(1,N+1))
    while q:
        ret.append(q.popleft())
        if q:
            q.append(q.popleft())
    print(*ret)
# i/o
N = int(input())
solution(N)