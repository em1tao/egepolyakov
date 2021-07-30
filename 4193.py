f = open("27-67b.txt")
n = int(f.readline())
d =[0]*5
d2=[0]*5
summ = 0
for i in range(n):
    cur = []
    d2=[0]*5
    k, *numbers = map(int, f.readline().split())
    s = sum(numbers)
    for j in range(k):
        if numbers[j] % 2:
            cur.append(numbers[j])
        else:
            t=numbers[j]
            for p in range(5):
                d2[(t+d[p])%5]=t+d[p]
            if d2[t% 5] ==0 or (d2[t%5]>t):
                d2[t%5]=t
            for p in range(5):
                if (d2[p]>0) and (d[p]==0 or d[p]>d2[p]):
                    d[p]=d2[p]
            d2 = [0] * 5
    if (len(cur) == 0):
        pass
    cur.sort()
    if len(cur) % 2 == 1:
        s -= cur[0]
        odd=cur[0]
        for j in range(1,len(cur)):
            t = cur[j]-odd
            for p in range(5):
                d2[(t + d[p]) % 5] = t + d[p]
            if d2[t % 5] == 0 or (d2[t % 5] > t):
                d2[t % 5] = t
            for p in range(5):
                if (d2[p] > 0) and (d[p] == 0 or d[p] > d2[p]):
                    d[p] = d2[p]
            d2 = [0] * 5
        for j in range(1, len(cur)):
            for k in range(j+1, len(cur)):
                t = cur[j] +cur[k]
                for p in range(5):
                    d2[(t + d[p]) % 5] = t + d[p]
                if d2[t % 5] == 0 or (d2[t % 5] > t):
                    d2[t % 5] = t
                for p in range(5):
                    if (d2[p] > 0) and (d[p] == 0 or d[p] > d2[p]):
                        d[p] = d2[p]
                d2 = [0] * 5
    else:
        for j in range(len(cur)):
            for k in range(j+1, len(cur)):
                t = cur[j] + cur[k]
                for p in range(5):
                    d2[(t + d[p]) % 5] = t + d[p]
                if d2[t % 5] == 0 or (d2[t % 5] > t):
                    d2[t % 5] = t
                for p in range(5):
                    if (d2[p] > 0) and (d[p] == 0 or d[p] > d2[p]):
                        d[p] = d2[p]
                d2 = [0] * 5
    summ += s
print(d)
d[0]=d[1]+d[2]
if (summ%5==0):
    print(summ)
    summ-=min(d)
print(summ)
