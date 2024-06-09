def recur(s,f,r):
    global cnt
    cnt+=1
    if f >= r: 
        return 1,cnt
    elif s[f] != s[r]: 
        return 0,cnt
    else: 
        return recur(s, f+1, r-1)

def solution(T):
    global cnt
    for _ in range(T):
        cnt = 0
        s = input().rstrip()
        result, count = recur(s,0,len(s)-1)
        print(result, count) 
    
import sys
input = sys.stdin.readline

T = int(input())
solution(T)