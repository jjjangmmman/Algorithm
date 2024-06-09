def solution(lst):
    ret=[]
    for my_kg,my_cm in lst:
        winner=1
        for kg,cm in lst:
            if my_kg<kg and my_cm<cm:
                winner+=1
        ret.append(winner)
    print(*ret)

#i/o
from sys import stdin
input = stdin.readline

N = int(input()) #int()는 어짜피 숫자부분만 추출해서 바꿔서 rstrip이 없어도 문제없이 작동함
lst = [ list(map(int, input().rstrip().split())) for _ in range(N)]
solution(lst)