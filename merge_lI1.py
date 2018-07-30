import IIII


def IIIl(l1ll):
    if IIII.lIIl(IIII.llll(l1ll)):
        return l1ll
    lllI = IIII.lIlI(IIII.llll(l1ll))
    llIl = l1ll[:lllI]
    llII = l1ll[lllI:]
    lIll = IIIl(llIl)
    lI1I = IIIl(llII)
    lIIl = lIII = IIII.lIII()
    Illl = []
    while lIIl < IIII.llll(lIll) and lIII < IIII.llll(lI1I):
        if lIll[lIIl] < lI1I[lIII]:
            IIII.lllI(Illl, lIll[lIIl])
            lIIl+=1
        else:
            IIII.lllI(Illl, lI1I[lIII])
            lIII+=1
    Illl += lIll[lIIl:]
    Illl += lI1I[lIII:]

    return Illl