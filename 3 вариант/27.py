f = open("27-31b.txt","r")
n = int(f.readline())
m = 9
d = 1000
summ = 0
for i in range(n):
    k1, k2, k3 = map(int, f.readline().split())
    a, c = max(k1,k2,k3), min(k1,k2,k3)
    b = k1 + k2 + k3 - a - c
    summ += b + c
    r1 = a - b
    if r1 < d and r1 != 9: d = r1

print(summ if summ % 9 != 0 else summ + d)
