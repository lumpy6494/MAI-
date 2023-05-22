from __init__ import np


def parn_sr (matrix):
    NN = np.full((len(matrix), len(matrix) * 2), 0.0)
    NM = np.full((len(matrix), len(matrix)*2), 0.0)
    for el in range(len(matrix)):
        i=0
        for val in range(len(matrix)*2):
            if val % 2 == 0:
                NM[el, val] = matrix[el]
            else:
                NM[el, val] = matrix[i]
                i=i+1
    for e in range(len(matrix)):
        for va in range(len(matrix) * 2):
            if va % 2 == 0:
                NN[e, va] = NM[e,va]/(NM[e,va]+NM[e,va+1])
            else:
                NN[e, va] = NM[e, va] / (NM[e, va] + NM[e, va - 1])
    # print(NM)
    return NN



