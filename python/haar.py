import numpy as np
import math
 
def haar_basis_slow(level, n):
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
   
def haar_level_slow(f, level):
    V, W = haar_basis_slow(level, f.shape[1])
    '''print("----\nlevel " + str(level) + "\n")
    print(V)
    print(W)
    print("----\n")'''
    an = (f * V) * V.getT()
    dn = (f * W) * W.getT()
    return an, dn

def haar_slow(f):
    n = int(math.log(f.shape[1], 2))
    #print(n)
    A = np.matrix(f[:2**(n-1)])
    #print(A)
    res = []
    for i in range(1,n+1):
        A, D = haar_level_slow(A, i)
        res.append(D)
    res.append(A)
    return res
    
'''
data = np.matrix([4,6,10,12,8,6,5,5])
A1, D1 = haar_level_slow (data, 1)
print(A1)
print(D1)

A2, D2 = haar_level_slow (A1, 2)
print(A2)
print(D2)
res = haar_slow(data)
print(res)
'''

def haar_level(f):
    base = 1 / 2**0.5
    n = len(f) // 2
    A = [base*(f[2*i] + f[2*i+1]) for i in range(0, n)]
    D = [base*(f[2*i] - f[2*i+1]) for i in range(0, n)]
    return A, D
    

def haar(f):
    n = int(math.log(len(f), 2))
    A = f[:2**(n)]
    res = []
    while True:
        A, D = haar_level(A)
        res.append(D)
        if len(D) == 1:
            res.append(A)
            break
    res.reverse()
    return res

def inverse_haar_level(a, d):
    res = []
    base = 1 / 2**0.5
    for i in range(0, len(a)):
        res.append(base*(a[i] + d[i]))
        res.append(base*(a[i] - d[i]))
    return res


def inverse_haar(h):
    an = h[0]
    for i in range(1, len(h)):
        an = inverse_haar_level(an, h[i])
    return an

data = [4,6,10,12,8,6,5,5]
print(data)
res = haar(data)
print(res)
print(inverse_haar(res))



























