def solution(s):
    answer = [0 for _ in range(26)]
    for ch in s:
        answer[ord(ch)-97]+=1
    return " ".join(map(str,answer))
    
#i/o
s=input()
print(solution(s))

#<시간복잡도가 더 큼>
def solution(s):
    from collections import Counter
    c = Counter(s)
    answer = [c[chr(i+97)] for i in range(26)]
    return " ".join(map(str,answer))
    
#i/o
s=input()
print(solution(s))
