def dbc_open (loc):
    from csv import reader
    o = open (loc,'r')
    dic = dict()
    with o as p:
        fil = list(reader(p))
        for q in fil :
            dic[q[0]] = q[1:]
    o.close()
    return dic


#print (dbc_open("D:\e.csv"))
