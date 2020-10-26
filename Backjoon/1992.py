from sys import stdin

input = stdin.readline
n = int(input())
arr = []

def quad(x,y,nx,ny,n):
    global arr
    if n == 1:
        return str(arr[y][x])
    check = False
    for i in range(y,ny):
        tmp = arr[y][x]
        for j in range(x,nx):
            if tmp != arr[i][j]:
                check = True
    if check:
        h = n//2
        a=quad(x,y,x+h,y+h,h)
        b=quad(x+h,y,x+n,y+h,h)
        c=quad(x,y+h,x+h,y+n,h)
        d=quad(x+h,y+h,x+n,y+n,h)
        return "("+a+b+c+d+")"
    else:
        return str(arr[y][x])




for _ in range(n):
    arr.append(list(map(int,input().rstrip('\n'))))
print(quad(0,0,n,n,n))