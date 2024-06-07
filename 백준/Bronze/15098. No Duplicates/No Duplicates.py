def solution(S):
    repeat_set = set()
    for s in S.split():
        if s in repeat_set:
            print("no")
            return 0
        else:
            repeat_set.add(s)
    print("yes")
# i/o
S = input()
solution(S)