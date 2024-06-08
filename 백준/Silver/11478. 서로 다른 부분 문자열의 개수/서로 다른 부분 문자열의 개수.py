def solution(S):
    subset=set()
    length = len(S)
    for step in range(1,length+1):
        for i in range(length-step+1):
            subset.add(S[i:i+step])
    return len(subset)
    
# i/o
import sys
S = input()
print(solution(S))