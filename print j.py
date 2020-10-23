

def print_unit(x):
    a = len(x)
    print  (str('-'*(a+2)) + '\n' + '|' + x + '|' + '\n' + str('-'*(a+2)))

def print_j(x):
    n = 0
    vaz = 1
    dicl = list()
    dic = {1:'_',2:'|',3:''}
    while x[n] != '!?':
        dic[1] += '_'*(len(x[n])+1)
        n += 1
    n = 2
    for q in x :
        if q != '!?':
            if q == '':
                dic[n] += ('  ')
                dic[n+1] += ('--')
                vaz = 0
            else:
                if vaz == 0:
                    dic[n] += '|'
                dic[n] += (q+'|')
                dic[n+1] += '-'*(len(q)+1)
                vaz = 1
        else:
            n += 2
            dic[n] = '|'
            dic[n+1] = ''
    for q in range(1,int((len(dic)-1)/2)):
        r = (q*2) + 1
        dic[r] += '-'
        if len (dic.get(r-1,100000)) < len (dic.get(r+1,0)):
            dic[r] = dic.get(r) + ('_' * int(len (dic.get(r+1,0)) - len (dic.get(r-1,100000)))) 
    for q in dic:
        dicl.append(dic[q])
    dicl.remove('|')
    print ('\n'.join(dicl))



def print_l (x):
    lis = list()
    
    m = 0
    for t in x :
        if len(t) > m:
            m = len(t)
    lis.append('_'*(m+2))
    for t in x:
        if( m - len(t)) > 0 :
            if ( m - len(t))%2 == 0:
                zzz = str(' '*int( (m - len(t))/2))
                
                lis.append('|' + zzz + str(t) + zzz + '|')
            else :
                
                zzz = str(' '*int( (m - len(t))/2))
                lis.append('| ' + zzz + t + zzz + '|') 
        else:
            lis.append('|'+t+'|')
    lis.append('#'*(m+2))
    q = '\n'.join(lis)
    print(q)
        



print_l(['c','w','','n','ggg'])