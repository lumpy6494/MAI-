from __init__ import np

def result(E):
    S = 0
    n1 = len(E)
    SE = np.zeros(n1)
    for n in range(n1):
        s = 0
        for k in range(n1):
            s = s + (E[n, k])
        S = S + s
        SE[n] = s
    SE = SE / S
    return SE



def norm_summ(vektor):
    result = np.zeros(len(vektor))
    summ = 0
    for i in vektor:
        summ=summ+i
    for n in range(len(vektor)):
        result[n] = vektor[n]/summ

    return result



