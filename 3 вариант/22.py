for x in range(10000,0,-1):
    r = x
    L = 0 
    M = 0
    while x > 0 : 
        L = L+1
        if M < (x % 10): 
            M = x % 10
        x = x // 10
    if L==3 and M==7:
        print(r)
        break