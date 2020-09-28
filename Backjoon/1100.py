from sys import stdin

input = stdin.readline

arr = [
    [1,0,1,0,1,0,1,0],
    [0,1,0,1,0,1,0,1],
    [1,0,1,0,1,0,1,0],
    [0,1,0,1,0,1,0,1],
    [1,0,1,0,1,0,1,0],
    [0,1,0,1,0,1,0,1],
    [1,0,1,0,1,0,1,0],
    [0,1,0,1,0,1,0,1],
]
board = []
cnt = 0
for i in range(8):
    
    tmp = list(input().rstrip('\n'))
    for j,v in enumerate(tmp):
        if v == 'F' and arr[i][j] == 1:
            cnt += 1
print(cnt)


