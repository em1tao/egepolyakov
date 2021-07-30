f = open("4203.txt")
n = int(f.readline())
cols = 10
rows = 7
d = [[0] * cols for i in range(rows)]
summ = 0
for i in range(n):
    cur = [[0] * cols for v in range(rows)]
    k1, k2, k3 = map(int,f.readline().split())
    a, c = max(k1,k2,k3), min(k1,k2,k3)
    b = k1 + k2 + k3 - a - c
    r1, r2 = a - c, b - c
    summ += a + b
    for z in range(rows):
        for x in range(cols):
            temp_summ = d[z][x] + r1
            cur[temp_summ%rows][temp_summ%cols] = temp_summ
    for z in range(rows):
        for x in range(cols):
            temp_summ = d[z][x] + r2
            cur[temp_summ%rows][temp_summ%cols] = temp_summ
    for z in range(rows):
        for x in range(cols):
            if cur[z][x] < d[z][x] and cur[z][x] or not d[z][x]:
                d[z][x] = cur[z][x]
                

print(*d, sep="\n")
print(summ if summ%7==3 or summ%7==5 and not (summ%7==3 and summ%7==5) else summ-d[summ%rows][summ%cols])
    
