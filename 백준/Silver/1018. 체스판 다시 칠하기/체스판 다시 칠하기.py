from collections import deque
from itertools import product

def cut_88_board(N,M): #combo는 sr,sc 시작인덱스를 반환
    row = range(N - 7)
    column = range(M - 7)
    for combo in product(row, column):
        yield combo
        
def cnt_rewrite(sr,sc,board):
    miss = 0
    chess = deque(("WB"*4+"BW"*4)*4)
    for i in range(8):
        for x in board[sr+i][sc:sc+8]:
            if x != chess.popleft(): 
                miss += 1
    return min(miss,64-miss)
        
    
def solution(N,M):
    min_lst = []
    for sr, sc in cut_88_board(N, M):
        min_lst.append(cnt_rewrite(sr, sc, board))
    return min(min_lst)
        
# i/o
N,M = map(int,input().split())
board = [input() for _ in range(N)]
print(solution(N,M))