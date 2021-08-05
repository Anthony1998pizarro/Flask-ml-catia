import numpy as np
import math
def coseno(documento,vocabulario):
    documento.insert(0,vocabulario)
    documento.insert(2,documento)
    N = len(documento)
    idf_tf = []
    for k in range(len(vocabulario)):
        pal = vocabulario[k]
        a1 = [pe(tok.count(pal)) for tok in documento]
        
        df = 0
        for i in a1:
            if i != 0:
                df += 1
        
        op= [e * idf_M(N, df) for e in a1]
        idf_tf.append(op)

    modul = []
    for i in range(len(idf_tf[0])):
        t = 0
        for j in range(len(idf_tf)):
            t += idf_tf[j][i] ** 2
        modul.append(m(t))
    
    logaritmo = [[resM(idf_tf[j][i], modul[i]) for j in range(len(idf_tf))]for i in range(len(idf_tf[0]))]
    matrizT = [[cose(ks, kr) for ks in logaritmo] for kr in logaritmo]
    return  np.array(matrizT)[1, 0]


def pe(n):
    if n > 0:
        return round(1 + math.log10(n), 2)
    else:
        return 0

def idf_M(n, df):
    if df > 0:
        return round(math.log10(n/df), 3)
    else:
        return 0

def m(j):
    return math.sqrt(j)


def cose(h1, h2):
    return round(sum(h1[i] * h2[i] for i in range(len(h1))), 2)

def resM(h1,m):
    if m == 0:
        return 0
    else:
        return round(h1/m,3)