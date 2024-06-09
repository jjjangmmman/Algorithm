import sys
    
info=[]
i=0
for line in sys.stdin.readlines()[1:]:
    i+=1
    age,name = line.rstrip().split()
    age = int(age)
    info.append([age,name,i])
info.sort(key=lambda x:(x[0],x[2]))
for member in info:
    print(member[0],member[1])