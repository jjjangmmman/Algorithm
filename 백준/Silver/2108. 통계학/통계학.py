from collections import Counter
import sys
input = sys.stdin.readline
N = int(input())
A = [int(input()) for _  in range(N)]

print(round(sum(A)/N))
A.sort()
print(A[N//2])
if N==1:
    print(A[0])
else:
    c = Counter(A).most_common(2)
    if c[0][1] == c[1][1]:
        print(c[1][0])
    else:
        print(c[0][0])
print(max(A)-min(A))