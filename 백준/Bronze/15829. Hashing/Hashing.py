D={}
for i in range(1,27):
    D[chr(i+96)] = i

input() #버리기 
S = input()

print(sum( D[s]*(31**i) for i,s in enumerate(S)) % 1234567891)
    