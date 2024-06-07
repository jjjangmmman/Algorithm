def solution(lines):
    index = 0
    cnt = 0
    while index<len(lines):
        cnt+=1
        D = {}
        n = int(lines[index].strip())
        for line in lines[index+1:index+1+n]:
            D[line.strip()] = 1
        print(f"Week {cnt} {len(D.keys())}")
        index+=n+1     
# i/o
import sys
lines = sys.stdin.readlines()[:-1]
solution(lines)