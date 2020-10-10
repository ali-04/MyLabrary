



def adad_avval (y) :
    qwe = list()
    for zx in range (2,y):
        vb = 0
        for zzx in range (2,zx):
            if zx % zzx == 0 :
                vb += 1
        if vb == 0 :
            qwe.append (zx)
    
    return qwe
    


def taj(y) :
    wer = []
    oi = y
    if y == 2 :
        return [2]
    elif y == 3:
        return [3]
    elif y == 4:
        return [2,2]
    if y == 1:
        return [1]
    qp = adad_avval (round(y/2)+2)
    qp.append (y)
    for not1 in qp:
        
        while oi % not1 == 0 :
            wer.append (not1)
            oi = int (oi / not1)










