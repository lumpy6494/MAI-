from __init__ import np


def svertka_oc (matrix1, matrix2, matrix3, matrix4):
    Res = np.full((6, 12), 0.0)
    for e in range(6):
        for va in range(12):
            Res[e, va] = matrix4[0]*matrix1[e,va]+ matrix4[1]*matrix2[e,va] + matrix4[2]*matrix3[e,va]
    return Res



def norm_svertka_oc(matrix):
    RR = np.full((6, 12), 0.0)
    for e in range(6):
        for va in range(12):
            if va % 2 == 0:
                RR[e, va] = matrix[e,va]/(matrix[e,va]+matrix[e,va+1])
            else:
                RR[e, va] = matrix[e, va] / (matrix[e, va] + matrix[e, va - 1])
    return RR


def summ_one_st(matrix, N):
    res = np.zeros(N)
    for e in range(N):
        summ = 0.0
        for va in range(N*2):
            if va % 2 == 0:
                summ = summ + matrix[e,va]
        res[e] =summ
    return res




