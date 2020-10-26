from sys import stdin

input = stdin.readline
a,b,v = map(int,input().split())

ans = (v-b-1) // (a-b) +1
print(ans)