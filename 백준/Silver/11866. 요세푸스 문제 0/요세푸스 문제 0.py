from collections import deque

def solution(N,K):
    ret=[]
    rot_num = -K+1
    q = deque(range(1,N+1))
    for _ in range(N):
        q.rotate(rot_num)
        ret.append(q.popleft())
    print("<", end="")
    print(*ret, sep=", ", end="")
    print(">")
# i/o
N,K = map(int, input().split())
solution(N,K)