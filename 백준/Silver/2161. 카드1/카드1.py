from collections import deque

def solution(N):
    ret=[]
    q = deque(range(1,N+1))
    for _ in range(N-1):
        ret.append(q.popleft())
        q.append(q.popleft())
    ret.append(q.popleft())
    print(*ret)
# i/o
N = int(input())
solution(N)