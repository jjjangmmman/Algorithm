from collections import deque

def solution(N):
    if N == 1:
        return 1
    alive = N-1
    q = deque(range(2,N+1))
    for i in range(2,N):
        q.rotate(-((i**3-1) % alive))
        q.popleft()
        alive-=1
    return q.popleft()
# i/o
N = int(input())
print(solution(N))