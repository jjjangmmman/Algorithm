N = int(input())
result = []

q1, r1 = divmod(N, 5)
while q1 >= 0:
    remainder = N - q1 * 5
    if remainder % 3 == 0:
        result.append(q1 + remainder // 3)
    q1 -= 1

if result:
    print(min(result))
else:
    print(-1)