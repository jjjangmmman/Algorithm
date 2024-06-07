def solution(owned_cards,search_cards):
    D={}
    ret = []
    
    for card in owned_cards.split():
        if card in D:
            D[card] += 1
        else:
            D[card] = 1
            
    for card in search_cards.split():
        ret.append( D[card] if card in D else 0) 
        
    return ret
    
# i/o
input()
owned_cards = input()
input()
search_cards = input()
print(*solution(owned_cards,search_cards))