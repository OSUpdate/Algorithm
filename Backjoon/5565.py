import sys

total = int(sys.stdin.readline())
prices = []
for i in range(9):
    prices.append(int(sys.stdin.readline()))
print(total-sum(prices))