def solution(lines):
    dot_list = []
    for line in lines:
        dot_list.append(list(map(int,line.strip().split())))
    dot_list.sort(key=lambda item: (item[1], item[0]))
    for dot in dot_list:
        print(f"{dot[0]} {dot[1]}")
    
        
# i/o
import sys

lines = sys.stdin.readlines()[1:]
solution(lines)