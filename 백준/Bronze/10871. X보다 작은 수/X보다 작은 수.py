def solution(A, X):
  for a in A:
    if a < X:
      print(f"{a} " , end="")


#i/o
X = int(input().split()[1])
A = list(map(int, input().split()))
solution(A,X)