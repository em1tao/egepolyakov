a = []
for i in range(30):
    a.append([" "]*30)
for i in range(6):
    a[24-i**2][i]="//"
    for k in range((i-1)**2+1,i**2):
        a[24-k][i]="/"
for i in range(25):
    print(*a[i])