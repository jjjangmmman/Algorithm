import sys
input = sys.stdin.readline
 
def round2(num):
    return int(num) + (1 if num - int(num) >= 0.5 else 0)
 
n = int(input())

if n==0:
    print(0)
    
else:
    a = round2(n * 0.15)
    arr = sorted(int(input()) for _ in range(n))
    print(round2(sum(arr[a:n-a])/(n-2*a)))
