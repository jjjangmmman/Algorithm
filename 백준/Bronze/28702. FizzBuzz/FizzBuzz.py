def solution(lines):
    next_num = 0
    for i,line in enumerate(lines[::-1],1):
      if line.strip().isdigit():
          next_num = int(line.strip())+i
          break
    if next_num%15==0:
        print("FizzBuzz")
    elif next_num%3==0:
        print("Fizz")
    elif next_num%5==0:
        print("Buzz")
    else:
        print(next_num)
        
# i/o
import sys
lines = sys.stdin.readlines()

solution(lines)