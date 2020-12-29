from sys import stdin

input = stdin.readline

n,m = map(int,input().split())
lengths = list(map(int,input().split()))
lengths.sort()
maximum = max(lengths)
h = 0
def bfind(find,start,end):
    global lengths
    if start > end:
        return
    mid = (start+end) // 2
    if lengths[mid] == find:
        return mid
    elif lengths[mid] > find:
        return bfind(find,start,mid-1)
    else:
        return bfind(find,mid+1,end)

for i in range(n):
    tmp += (lengths[i] - h)
