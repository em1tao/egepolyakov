def calc(x,y):
    if x==y:
        return 1
    if x > y:
        return 0
    return calc(x+1,y)+calc(x+3,y)+calc(x*2,y)
print(calc(3,15))
