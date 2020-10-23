from sys import stdin

input = stdin.readline
arr = []
ans = [0,0]
def quad(x,y,nx,ny,size):
    global arr,ans
    check = False
    
    cur = arr[y][x]
    if size == 1:
        ans[arr[y][x]] += 1
        return 
    for i in range(y,ny):
        for j in range(x,nx):
            if arr[i][j] != cur:
                check = True
                break

    if check:
        h = size // 2

        quad(x,y,x+h,y+h,h)
        quad(x+h,y,x+size,y+h,h)
        quad(x,y+h,x+h,y+size,h)
        quad(x+h,y+h,x+size,y+size,h)

    else:
        ans[arr[y][x]] += 1
        return
n = int(input())
for _ in range(n):
    arr.append(list(map(int,input().split())))

quad(0,0,n,n,n)
print(ans)