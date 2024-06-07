def solution(n,num_per_size,t,p):
  bundle_of_T = sum((size+(t-1))//t for size in num_per_size)
  bundle_of_P, each_of_P = divmod(n, p)
  
  print(bundle_of_T)
  print(bundle_of_P, each_of_P)
        
# i/o
n = int(input())
num_per_size = list(map(int,input().split()))
t,p = map(int,input().split())

solution(n,num_per_size,t,p)