for i in range(244143,1367822):
    div_c = 0
    for k in range(i//2,1,-1):
        if i % k == 0:
            div_c += 1
            if div_c <=2:
                print(k)
        if div_c > 5:
            break
    if div_c == 5:
        print(i)