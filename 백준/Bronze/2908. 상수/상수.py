def solution(a,b):
    return max(a,b)
# i/o
a,b = map(int, input()[::-1].split())
print(solution(a,b))