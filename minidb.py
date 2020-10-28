

def dbc_open (loc):
    
    from os import path
    from csv import reader

    if path.exists(loc):
        o = open (loc,'r')
        with o as p:
            fil = list(reader(p))
            o.close()
        return fil
    else:
        q = open (loc,'w+')
        q.close()

        return("it's first use")



#           |-------\           \      /            |-------
#           |        \           \    /             |
#           |        /            \  /              |
#           |-------/              \/               |-------
#           |       \              |                |
#           |        \             |                |
#           |        /             |                |
#           |-------/              |                |-------



def dbc_write (loc,lis):
    with open(loc,'w+') as File:

        for line in lis:
            q = ''
            
            
            for har_chiz in line:
                q += ( str(har_chiz) + ',')
            File.write(q[: len(q)-1 ])
            
            
            File.write('\n')
        
        File.close()



#dbc_write("/home/mohammad/Documents/GitHub/python/1.csv",[[1],['w',5]])

#print (dbc_open("D:\e.csv"))

