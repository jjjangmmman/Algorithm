"""
1. 아이디어
- 재귀함수 안에서, s[0]과 s[-1]이 같으면 다음 비교를 위해 재귀 호출
- 문자열의 front가 rear와 같거나 커지면 모든 문자열의 팰린드롬 여부를 확인했으므로 return 1
- s[front]와 s[rear]가 다르면 팰린드롬이 아니므로 return 0

2. 시간 복잡도
- O(T * n) > 가능

3. 자료구조
- 호출 횟수를 셀 cnt 을 전역함수로 선언 global

"""

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
