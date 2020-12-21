from sys import stdin

input = stdin.readline

t = int(input())

for i in range(t):
    h,w,n = map(int,input().split())
    room = n//h+1
    floor = n%h
    if floor == 0:
        floor = str(h)
        room -= 1
    floor = str(floor)
    room = str(room)
    print(floor+room.zfill(2))
    