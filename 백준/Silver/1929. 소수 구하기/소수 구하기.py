M, N = map(int, input().split())

def is_prime(num):
    if num < 2:
        return False
    if num == 2 or num==3:
        return True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

for num in range(M, N + 1):
    if is_prime(num):
        print(num)