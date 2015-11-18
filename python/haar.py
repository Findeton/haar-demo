import numpy as np
import math
 
def haar_basis(level, n):
    base = 1/2**0.5
    V = []
    W = []
    exp = 2**level
    loopN = n//exp
    exp = exp//2
    basen = base**level
    #print("base " + str(base) + " exp " + str(exp) + " basen " + str(basen))
    for i in range(loopN):
         W.append([0, 0] * exp * i + [basen] * exp + [-basen] * exp + [0, 0] * exp * (loopN - i - 1))
         V.append([0, 0] * exp * i + [basen, basen] * exp  + [0, 0] * exp * (loopN - i - 1))
    return np.matrix(V).getT(), np.matrix(W).getT()
   
def haar_level(f, level):
    V, W = haar_basis(level, f.shape[1])
    '''print("----\nlevel " + str(level) + "\n")
    print(V)
    print(W)
    print("----\n")'''
    an = (f * V) * V.getT()
    dn = (f * W) * W.getT()
    return an, dn

def haar(f):
    n = int(math.log(f.shape[1], 2))
    #print(n)
    A = np.matrix(f[:2**(n-1)])
    #print(A)
    res = []
    for i in range(1,n+1):
        A, D = haar_level(A, i)
        res.append(D)
    res.append(A)
    return res
    
'''
data = np.matrix([4,6,10,12,8,6,5,5])
A1, D1 = haar_level (data, 1)
print(A1)
print(D1)

A2, D2 = haar_level (A1, 2)
print(A2)
print(D2)
res = haar(data)
print(res)
'''