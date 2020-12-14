from sys import stdin

input = stdin.readline

direct = [(1,2),(-1,2),(2,1),(2,-1),(-2,1),(-2,-1),(-1,-2),(1,-2)]
start = list(input().rstrip('\n'))
start = [ord(start[0])-97,int(start[1])-1]
count = 0
print(start)
for ny,nx in direct:
    nx += start[1]
    ny += start[0]
    if 0<=nx<8 and 0<=ny<8:
        print(nx,ny)
        count += 1
print(count)