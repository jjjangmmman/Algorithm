import functools
import operator

N = int(input())
rs = functools.reduce(operator.mul, range(1,N+1), 1)
cnt=0
while rs%10==0:
    cnt+=1
    rs//=10
print(cnt)