def com (dos,ch):


    do = dos * 100

    nbox = ch * 2

    coms = nbox*do // 100

    dobs = coms // 2

    one  = coms % 2

    nons = ch - one - dobs

    retn = "[%s%s%s]"%('='*int(dobs),'-'*int(one),' '*int(nons))

    return retn