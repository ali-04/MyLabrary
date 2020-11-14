

def uni (li):
    qo = li[0]
    ser = []
    for v in qo:
        dae = 1
        for vvc in li[1:]:
            if not(v in vvc) :
                dae = 0
        if dae == 1 :
            ser .append(v)
    return ser


p = 1