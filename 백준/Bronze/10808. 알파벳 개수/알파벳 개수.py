def solution(s):
    answer = [0 for _ in range(26)]
    for ch in s:
        answer[ord(ch)-97]+=1
    return " ".join(map(str,answer))
    
#i/o
s=input()
print(solution(s))