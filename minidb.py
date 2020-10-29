


Rr = lambda x : ','.join(x)







def blist (lis,x):
    if len(lis) > x :
        return True 
    else:
        return False 



def alist (lis,x,y):
    for q in range (0, x - len(lis) +1 ):
        lis.append (y)





def dbc_open (loc):
    
    #    from os import path
    from csv import reader

    
    o = open (loc,'r')
    with o as p:
        fil = list(reader(p))
        o.close()
    return fil
    


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
            q = list()
            
            
            for har_chiz in line:
                q.append ( str(har_chiz) )
            File.write(Rr(q))
            
            
            File.write('\n')
        
        File.close()








def dbc (name,code) :
    
    from os import path
    from os import getcwd

    loc = str( getcwd() ) + '\\' + ('%s.csv' %name)

    if not ( path.exists(  loc  ) ) :
        q2 = open (loc,'w+')
        q2.close 


    if type(code) == str :
        if code == 'open':    
            return dbc_open(loc)


    elif type(code) == list :
        liscode = code[1:]
        code = code[0]
            

        if code == 'edit' :
                
            fFile = dbc_open(loc)
            for q in liscode:

                if not ( blist(fFile , int(  q[0]  ) ) ):
                    alist ( fFile , int(  q[0]  ) , str() )


                fFile [ int(  q[0]  ) ] = q[1:]
                dbc_write(loc,fFile)





#dbc('q',['edit',['2','9']])


#dbc_write("/home/mohammad/Documents/GitHub/python/1.csv",[[1],['w',5]])

#print (dbc_open("D:\e.csv"))

