import sys

con = True
while con:
    length = list(map(int,sys.stdin.readline().split()))
    if sum(length) == 0:
        con = False
        break
    state = "right" if length[0]**2 + length[1]**2 == length[2]**2 or length[0]**2 + length[2]**2 == length[1]**2 or length[1]**2 + length[2]**2 == length[0]**2 else "wrong"
    print(state)