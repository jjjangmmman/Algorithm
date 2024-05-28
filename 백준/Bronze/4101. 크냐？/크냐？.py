def solution(x,y):
  return "Yes" if x>y else "No"

#i/o
import sys
input = sys.stdin.readline

while True:
  try:
      x, y = map(int, input().strip().split())
      if (x, y) == (0, 0): 
          break
      print(solution(x, y))
  except EOFError:
      break