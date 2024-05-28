def solution(A,v):
  cnt=0
  for a in A:
    if a==v:
      cnt+=1
  return cnt

#I/O
input()
A = list(map(int,input().split()))
v = int(input())

print(solution(A,v))