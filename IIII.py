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