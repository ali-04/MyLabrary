

def print_unit(x):
    a = len(x)
    print  (str('-'*(a+2)) + '\n' + '|' + x + '|' + '\n' + str('-'*(a+2)))

def print_j(x):
    n = 0
    dicl = list()
    dic = {1:'_',2:'|',3:''}
    while x[n] != '!?':
        dic[1] += '__'
        n += 1
    n = 2
    for q in x :
        if q != '!?':
            dic[n] += (q+'|')
            dic[n+1] += '-'*(len(q)+1)
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






