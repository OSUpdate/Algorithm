from sys import stdin

input = stdin.readline

n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
start = 0
end = max(arr)

def bfind(find,start,end):
    global arr
    mid = (start+end) // 2
    tmp = 0
    for i in arr:
        if i-mid < 0:
            tmp += 0
        else:
            tmp += (i-mid)
    if tmp == find:
        return mid
    elif tmp > find:
        return bfind(find,mid+1,end)
    else:
        return bfind(find,start,mid-1)

while start <= end:
    tmp = 0
    mid = (start+end)//2
    for i in arr:
        if i> mid:
            tmp += (i-mid)
    if tmp < start:
        end = mid -1
    else:
        answer = mid
        start = mid+1
print(bfind(m,0,end))