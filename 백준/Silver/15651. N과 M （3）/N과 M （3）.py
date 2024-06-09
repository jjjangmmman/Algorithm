"""

1. 아이디어
- 백트래킹 재귀함수 안에서, for문을 돌면서 1~N 숫자 선택 (중복 가능이므로 방문 여부 확인 x)
- 재귀함수에서 M개를 선택할 경우 print

2. 시간 복잡도
- N^N (n=8까지 가능) > 가능

3. 자료구조
- 결과값을 저장할 int[]

"""
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
rs = []

def recur(num): #num은 재귀과정을 트리로 표현했을때 depth라고 생각 
    if num==M:
        print(*rs)
        return
    for i in range(1,N+1):
        rs.append(i)
        recur(num+1)
        rs.pop()
recur(0)