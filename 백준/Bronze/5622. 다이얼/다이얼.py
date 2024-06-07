def parse_log(ch):
    A = ["ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]
    for sec,sub_str in enumerate(A,3):
        if ch in sub_str:
            return sec

def solution(alphabets):
    total_time=0
    for sec in map(parse_log, alphabets):
        total_time+=sec
    return total_time
# i/o
alphabets = input()
print(solution(alphabets))