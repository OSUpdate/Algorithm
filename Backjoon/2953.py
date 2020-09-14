from sys import stdin
input = stdin.readline

arr = []
for i in range(5):
    n1,n2,n3,n4 = map(int,input().split())
    arr.append(n1+n2+n3+n4)
print("%d %d"% (arr.index(max(arr)) + 1,max(arr)))