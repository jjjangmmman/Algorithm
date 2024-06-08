value = input() 
N = int(value)
length = len(value) #입력값이 몇자리 수인지
result=0
start = max(1, N - length * 9)  # 시작값이 1보다 작지 않도록 보정 중요!
for n in range(start,N):
    if n+sum(map(int,str(n)))==N:
        result=n
        break;
print(result)