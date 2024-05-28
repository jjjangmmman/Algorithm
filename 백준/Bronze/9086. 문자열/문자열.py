def solution(lines):
    for line in lines:
        line = line.strip()
        print(line[0]+line[-1])
#i/o
import sys
lines = sys.stdin.readlines()
lines = lines[1:]
solution(lines)