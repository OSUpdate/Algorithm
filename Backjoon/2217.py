from sys import stdin

input = stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()
for i in range(n):
    arr[i] = (n-i)*arr[i]
print(max(arr))