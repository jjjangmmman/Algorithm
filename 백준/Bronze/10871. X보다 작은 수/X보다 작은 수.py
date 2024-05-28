# <1>
l, std = map(int,input().split())
arr = list(map(int,input().split()))
result = [str(a) for a in arr if a<std]
print(' '.join(result))

# <2>
def solution(A, X):
  answer = []
  for a in A:
    if a < X:
      answer.append(str(a))
  print(" ".join(answer))


#i/o
N,X = map(int,input().split())
A = list(map(int, input().split()))
solution(A,X)
