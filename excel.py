


def xread (loc,sheet):

    from pandas import read_excel
    from pandas import DataFrame

    df = read_excel ( loc , sheet_name=sheet )
    dic = dict()
    w = 0

    for q in df:
        w += 1

    h = len(str(DataFrame(df, columns = [w])).splitlines())


    for q in range(0,h+1):
        
        dic[q] = {}
        for qq in range(0,w+1):
            
            indate =  '  '.join (str (DataFrame(df ,index= [q] ,columns= [qq] )).splitlines() [1].split('  ') [1:])
            dic[q][qq] = indate


    #    for qq0 in pq :

            #indate =   pd.DataFrame(df, index= [q] ,columns= [])
            
        #    qq = qq0.split('  ')
        #    dic[    qq[0]  ] = dic.get( qq[0], [] ) + qq[1:]
    return dic


#p = 2





#p = (xread (r"C:\users\ali\hello_world.xlsx",'1'))

#q = 0









