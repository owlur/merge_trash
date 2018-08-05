def llll(lllI):
    return len(lllI)

def lllI(llII, IIII):
    llII.append(IIII)

def lIlI(llII):
    return llII // 2

def lIII():
    return 0

def lIIl(llII):
    return llII <= 1


def aMM(l):
    return ('',len(l) // 2)

class cMb:
    def cMP(self):
        pass

def ccccMMM(L,R,alist):
    i = j = 0
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            alist.append(L[i])
            i+=1
        else:
            alist.append(R[j])
            j+=1
    return i,j

def dpcccccIMMMMMMMMMMMMMMM(alist):
    for _ in range(len(alist)//2):
        alist.pop(0)