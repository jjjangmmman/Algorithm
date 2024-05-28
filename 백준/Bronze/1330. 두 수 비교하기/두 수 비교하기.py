<1>
a,b=map(int,input().split())
if a>b:
    print(">")
elif a<b:
    print("<")
else:
    print("==")

<2>
def solution(x,y):
  return ">" if x>y else "==" if x==y else "<"

#i/o
a,b=map(int,input().split())
print(solution(a,b))
