from sys import stdin

input = stdin.readline

def findNum(arr,num):
    start = 0
    end = len(arr) - 1

    mid = (start + end) // 2
    while end-start >= 0:
        if arr[mid] == num:
            return 1
        elif arr[mid] <= num:
            start = mid + 1
        else:
            end = mid - 1
        mid = (start+end)//2
    return 0
n = int(input())
farr = list(map(int,input().split()))
m = int(input())
marr = list(map(int,input().split()))
farr.sort()

for i in marr:
    print(findNum(farr,i))