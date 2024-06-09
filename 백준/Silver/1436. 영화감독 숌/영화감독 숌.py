def infinite_sequence():
    num = 666
    while True:
        yield num
        num += 1
        
def solution(N):
    no=0
    gen = infinite_sequence()
    for value in gen:
        if "666" in str(value):
            no+=1
            if no==N:
                print(value)
                break
# i/o
N = int(input())
solution(N)