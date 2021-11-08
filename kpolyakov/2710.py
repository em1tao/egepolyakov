f = open("27-24b.txt")
n = int(f.readline())
minraz = 10000
summ = 0
for i in range(n):
    k1,k2 = map(int,f.readline().split())
    a,b = max(k1,k2),min(k1,k2)
    summ += b
    r1 = a - b
    if r1 % 10 and r1 < minraz:
        minraz = r1

if str(summ)[-1] == "6":
    print(summ+minraz)
else:
    print(summ)
