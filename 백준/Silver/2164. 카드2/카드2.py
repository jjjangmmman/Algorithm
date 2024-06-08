from collections import deque

def solution(N):
    q = deque(range(1,N+1))
    for _ in range(N-1):
        q.popleft()
        q.append(q.popleft())
    return q.popleft()
# i/o
N = int(input())
print(solution(N))