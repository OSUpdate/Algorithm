import sys

n = 1000 - int(sys.stdin.readline())
cnt = 0
while n-500 >= 0:
    n-=500
    cnt+=1
while n-100 >= 0:
    n-=100
    cnt+=1
while n-50 >= 0:
    n-=50
    cnt+=1
while n-10 >= 0:
    n-=10
    cnt+=1
while n-1 >= 0:
    n-=1
    cnt+=1
print(cnt)