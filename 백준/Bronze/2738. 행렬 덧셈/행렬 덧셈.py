def solution(n,m,A,B):
  answer = [[""] * m for _ in range(n)]
  for i in range(n):
    for j in range(m):
      answer[i][j]=str(A[i][j]+B[i][j])
    print(" ".join(answer[i]))
  
#i/o
import sys
input = sys.stdin.readline

n,m=map(int,input().split())
a = [list(map(int,input().strip().split())) for _ in range(n)]
b = [list(map(int,input().strip().split())) for _ in range(n)]

solution(n,m,a,b)