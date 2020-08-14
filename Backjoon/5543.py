import sys
burger = []
beverage = []
total = 4000
tmp = 0
for i in range(3):
    burger.append(int(sys.stdin.readline()))
for j in range(2):
    beverage.append(int(sys.stdin.readline()))
for _,bg in enumerate(burger):
    for _,bv in enumerate(beverage):
        tmp = bg + bv - 50
        if total > tmp:
            total = tmp
        tmp = 0
print(total)