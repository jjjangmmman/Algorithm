def solution(n,arr):
  answer = [[0 for b in range(100)] for a in range(100)] 
  #[[0] * 100 for _ in range(100)]
  for index in range(n):
    x,y= arr[index]
    for i in range(x,x+10):
      for j in range(y,y+10):
        answer[i][j] = 1
  return sum( sum(row) for row in answer)
  #return sum(map(sum, answer))
    
        
# i/o
import sys
lines = sys.stdin.readlines()
n = int(lines[0].strip())
xy = [list(map(int,line.strip().split())) for line in lines[1:]]

print(solution(n,xy))
