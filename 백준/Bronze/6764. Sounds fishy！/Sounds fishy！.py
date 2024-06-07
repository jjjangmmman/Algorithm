def solution(depths):
    if len(set(depths)) == 1:
        print("Fish At Constant Depth")
    elif len(set(depths)) != 4:
        print("No Fish")
    elif depths == sorted(depths):
        print("Fish Rising")
    elif depths == sorted(depths,reverse=True):
        print("Fish Diving")
    else:
        print("No Fish")
# i/o
depths = [int(input()) for _ in range(4)]
solution(depths)