import IIII


def IIIl(llll):
    if IIII.llll(llll) <= 1:
        return llll
    lllI = IIII.llll(llll) // 2
    llIl = llll[:lllI]
    llII = llll[lllI:]
    lIll = IIIl(llIl)
    lIlI = IIIl(llII)
    lIIl = lIII = 0
    Illl = []
    while lIIl < IIII.llll(lIll) and lIII < IIII.llll(lIlI):
        if lIll[lIIl] < lIlI[lIII]:
            IIII.lllI(Illl, lIll[lIIl])
            lIIl+=1
        else:
            IIII.lllI(Illl, lIlI[lIII])
            lIII+=1
    Illl += lIll[lIIl:]
    Illl += lIlI[lIII:]
    return Illl