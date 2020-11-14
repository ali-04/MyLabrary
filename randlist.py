






def randlist(x):
    from random import randint
    y = x
    z = list()
    for q in range(0,len(x)):
        im = randint (0,len(y)-1)
        z.append (y[im])
        del (y[im])
    return z








#print(randlist([1,2,3,4,5]))










