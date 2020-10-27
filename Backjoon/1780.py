from sys import stdin

input = stdin.readline

n = int(input())
arr = []
ans = [0,0,0]
def quad(x,y,nx,ny,n):
    cur = arr[y][x]
    check = False
    if n == 1:
        ans[arr[y][x]+1] += 1
        return
    
    for i in range(y,ny):
        for j in range(x,nx):
            if cur != arr[i][j]:
                check = True
    if check:
        h = n//3
        quad(x,y,x+h,y+h,h)
        quad(x+h,y,x+(h*2),y+h,h)
        quad(x+(h*2),y,x+n,y+h,h)

        quad(x,y+h,x+h,y+(h*2),h)
        quad(x+h,y+h,x+(h*2),y+(h*2),h)
        quad(x+(h*2),y+h,x+n,y+(h*2),h)

        quad(x,y+(h*2),x+h,y+n,h)
        quad(x+h,y+(h*2),x+(h*2),y+n,h)
        quad(x+(h*2),y+(h*2),x+n,y+n,h)
    else:
        ans[arr[y][x]+1] += 1
        return
for _ in range(n):
    arr.append(list(map(int,input().split())))

quad(0,0,n,n,n)
[print(i) for i in ans]