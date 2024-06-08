def solution(n):
    ret = set()
    for i in range(n+1):
        for j in range(n+1):
            ret.add(tuple(sorted([i, j])))
    
    return sum(map(sum,ret))
# i/o
n = int(input())
print(solution(n))