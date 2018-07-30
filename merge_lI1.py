import IIII


def IIIl(llll):
    if IIII.lIIl(IIII.llll(llll)):
        return llll
    lllI = IIII.lIlI(IIII.llll(llll))
    llIl = llll[:lllI]
    llII = llll[lllI:]
    lIll = IIIl(llIl)
    lIlI = IIIl(llII)
    lIIl = lIII = IIII.lIII()
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