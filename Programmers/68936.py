def quad(arr,ans,x,y,nx,ny,size):
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

        quad(arr,ans,x,y,x+h,y+h,h)
        quad(arr,ans,x+h,y,x+size,y+h,h)
        quad(arr,ans,x,y+h,x+h,y+size,h)
        quad(arr,ans,x+h,y+h,x+size,y+size,h)

    else:
        ans[arr[y][x]] += 1
        return
def solution(arr):
    answer = [0,0]
    n = len(arr)
    quad(arr,answer,0,0,n,n,n)
    return answer