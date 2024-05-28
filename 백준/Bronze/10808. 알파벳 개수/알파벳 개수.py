def solution(s):
    from collections import Counter
    c = Counter(s)
    answer = [c[chr(i+97)] for i in range(26)]
    return " ".join(map(str,answer))
    
#i/o
s=input()
print(solution(s))