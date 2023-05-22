from __init__ import np
from norm import result

# Функция вычисления % критерия согласия
def harmony(MATRIX):
    n = len(MATRIX)
    sum_st=np.sum(MATRIX, axis=0)
    print(f"Сумма по столбцам = {sum_st}")
    norm = np.array(result(MATRIX))
    print(f"Сумма Нормализаций = {np.sum(norm)}")
    sum_Lmax = np.dot(sum_st, norm)
    print(f"LMAX = {sum_Lmax}")
    ic=(sum_Lmax-n)/(n-1)
    c = (ic / 0.58) * 100
    return c

def not_harm(MATRIX):
    value = MATRIX.item(0)
    if value < 0.1:
        return value
    else:
        return f"{MATRIX[0][0]} Матрица НЕ согласована!'"



# Функция вычисления собственных значений и критерия согласия
# Функция вычисления собственных значений и критерия согласия
# def harmony(MATRIX):
#  n=len(MATRIX)
#  a=np.linalg.eigvals(MATRIX)
#  print(a)
#  a=abs(a)
#  A=a.max()
#  c=(A-n)/(n-1)
#  return c