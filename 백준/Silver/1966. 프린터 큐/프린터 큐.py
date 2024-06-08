from collections import deque

def solution(T):
    for _ in range(T): #테스트 케이스 T번 반복
        a,b = map(int, input().rstrip().split()) # a = number_of_docs, b = index of search_doc
        lst = list(map(int, input().rstrip().split())) # lst = priority list
        q = deque(enumerate(lst)) # q's element structure -> (index, priority)
        cnt=0
        while q:
            index, priority = q[0]
            if priority == max(q, key=lambda x: x[1])[1]:
                q.popleft()
                cnt+=1
                if index==b:
                    print(cnt)
                    break
            else:
                q.append(q.popleft())
# i/o
import sys
input = sys.stdin.readline
T = int(input().rstrip())
solution(T)