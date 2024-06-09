"""
1. 아이디어
- 재귀함수 안에서, s[0]과 s[-1]이 같으면 다음 비교를 위해 재귀 호출
- 문자열의 front가 rear와 같거나 커지면 모든 문자열의 팰린드롬 여부를 확인했으므로 return 1
- s[front]와 s[rear]가 다르면 팰린드롬이 아니므로 return 0

2. 시간 복잡도
- O(T * n) > 가능

3. 자료구조
- 호출 횟수를 셀 cnt 변수
- 반환값과 호출 횟수를 저장할 rs[]

"""
def recur(s,f,r,cnt):
    if f >= r: 
        return [1,cnt]
    elif s[f] != s[r]: 
        return [0,cnt]
    else: 
        cnt+=1
        return recur(s, f+1, r-1,cnt)

def solution(T,rs):
    for _ in range(T):
        s = input().rstrip()
        rs = recur(s,0,len(s)-1,1)
        print(*rs) 
    
import sys
input = sys.stdin.readline

T = int(input())
rs = []
solution(T,rs)