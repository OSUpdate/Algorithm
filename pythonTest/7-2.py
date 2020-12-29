from sys import stdin

input = stdin.readline

n = int(input())
sell = list(map(int,input().split()))

m = int(input())
flist = list(map(int,input().split()))
sell.sort()

def bfind(find,start,end):
    global sell
    if start > end:
        return None
    mid = (start+end)//2
    if sell[mid] == find:
        return mid
    elif sell[mid] > find:
        return bfind(find,start,mid-1)
    else:
        return bfind(find,mid+1,end)
print(' '.join(['yes' if bfind(i,0,len(sell)-1) else 'no' for i in flist]))



