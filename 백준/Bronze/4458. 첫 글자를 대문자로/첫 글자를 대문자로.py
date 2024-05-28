def solution(lines):
    for line in lines:
        line = line.strip()
        print(line[0].upper()+line[1:])
#i/o
import sys
lines = sys.stdin.readlines()[1:]
solution(lines)

#대문자 소문자 관련 메서드
self.islower(), self.isupper() = T/F를 반환하며 문자열이 대/소문자인지 판단
self.lower(), self.upper() = 대/소문자로 변환한 문자열 반환
ex) s[0].upper = 대문자로 바뀐 s[0]만 반환한다 s전체 아님!

#메서드는 아니지만 파이썬 문자열의 특기 문자열 슬라이싱
[start:end:hop] 유용하게 사용하기!
