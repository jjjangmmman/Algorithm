def solution(s):
    n = len(s)//10
    for i in range(n+1):
        print(s[i*10:i*10+10])
#i/o
s = input()
solution(s)