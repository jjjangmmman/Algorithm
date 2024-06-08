def solution(N,M):
    N_set = set(N.split())
    ret = [1 if m in N_set else 0 for m in M.split()]
    print(*ret, sep='\n')
# i/o
input()
N = input()
input()
M = input()
solution(N,M)