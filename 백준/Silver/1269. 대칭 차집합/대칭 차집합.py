def solution(A,B):
    a = set(A.split())
    b = set(B.split())
    return len(a.symmetric_difference(b))
    
# i/o
input()
A = input()
B = input()
print(solution(A,B))