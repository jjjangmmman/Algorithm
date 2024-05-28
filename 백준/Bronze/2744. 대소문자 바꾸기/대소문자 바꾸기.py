def solution(s):
    # 문자열은 불변(immutable) 타입이기 때문에 인덱스를 사용하여 직접 변경할 수 없음
    # 따라서 문자열을 리스트로 변환하여 수정 가능하게
    s=list(s)
    for i,ch in enumerate(s):
        s[i] = ch.upper() if ch.islower() else ch.lower()
    return ''.join(s) #리스트를 다시 문자열로 반환
#i/o
s = input()
print(solution(s))

#아싸리 result=[]로 결과를 반환하는 빈 리스트를 만들어도됨