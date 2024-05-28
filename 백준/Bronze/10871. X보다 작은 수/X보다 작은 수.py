l, std = map(int,input().split())
arr = list(map(int,input().split()))
result = [str(a) for a in arr if a<std]
print(' '.join(result))