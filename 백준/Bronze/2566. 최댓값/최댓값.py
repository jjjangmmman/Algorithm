def solution(arr):
  answer, row, col = 0, 0, 0
  for i in range(9):
      tmp = max(arr[i])
      if tmp > answer:
          answer = tmp
          row = i
          col = arr[i].index(tmp)  # 최대값의 열 인덱스를 저장
  print(answer)
  print(f"{row + 1} {col + 1}") 

# i/o
import sys

lines = sys.stdin.read().strip().split('\n')
board = [list(map(int, line.split())) for line in lines]
solution(board)