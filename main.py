from __init__ import np
from norm import result, norm_summ
from harmory import harmony, not_harm
from parsr import parn_sr
from normal_svert import svertka_oc, norm_svertka_oc, summ_one_st

# Список Алтернатив
alt1 = ['Квартира на Лесной','Квартира на Звездной', 'Квартира на Невском',
        'Квартира на Богатырском', "Квартира на Комендантском", 'Квартира на Ладожской']

try:
    geo = input("Введите оцеку для критерия 'Местоположение':\n"
                "Нажать ENTER для продолжения...")
    geo=float(geo)

    home = input("Введите оцеку для критерия 'Характеристика жилого дома':\n"
                 "Нажать ENTER для продолжения...")
    home = float(home)

    kv = input("Введите оцеку для критерия 'Характеристика оцениваемой квартиры' :\n"
               "Нажать ENTER для продолжения...")
    kv = float(kv)

except ValueError:
    print("Ошибка преобразования типов")


# Матрица критериев
MC = np.mat([[geo/geo, geo/home, geo/kv],
             [home/geo, home/home, home/kv],
             [kv/geo, kv/home, kv/kv]])
print ('Матрица криетериев:')
print(MC)

# Вычисление критерия согласия Матрица криетериев
c=harmony(MC)
print ('Значение критерия согласия для матрицы 1-"Матрица криетериев":',not_harm(c))

CN=result(MC)
print('Нормированные результаты сравнения по критерию 1-"Матрица криетериев":',CN)

wait = input("Нажать ENTER для продолжения...")

# Местоположение
kv_lesnay=float(7)
kv_zvezdnay = float(9)
kv_nevskiy = float(8)
kv_bogat = float(6)
kv_komenda = float(5)
kv_lagoj = float(3)

MP = np.mat([[kv_lesnay/kv_lesnay, kv_lesnay/kv_zvezdnay, kv_lesnay/kv_nevskiy, kv_lesnay/kv_bogat, kv_lesnay/kv_komenda,kv_lesnay/kv_lagoj ],
             [kv_zvezdnay/kv_lesnay, kv_zvezdnay/kv_zvezdnay, kv_zvezdnay/kv_nevskiy, kv_zvezdnay/kv_bogat, kv_zvezdnay/kv_komenda, kv_zvezdnay/kv_lagoj ],
             [kv_nevskiy/kv_lesnay, kv_nevskiy/kv_zvezdnay, kv_nevskiy/kv_nevskiy, kv_nevskiy/kv_bogat, kv_nevskiy/kv_komenda, kv_nevskiy/kv_lagoj],
             [kv_bogat/kv_lesnay,kv_bogat/kv_zvezdnay,kv_bogat/kv_nevskiy,kv_bogat/kv_bogat,kv_bogat/kv_komenda,kv_bogat/kv_lagoj],
             [kv_komenda/kv_lesnay,kv_komenda/kv_zvezdnay,kv_komenda/kv_nevskiy,kv_komenda/kv_bogat,kv_komenda/kv_komenda,kv_komenda/kv_lagoj],
             [kv_lagoj/kv_lesnay,kv_lagoj/kv_zvezdnay,kv_lagoj/kv_nevskiy,kv_lagoj/kv_bogat,kv_lagoj/kv_komenda,kv_lagoj/kv_lagoj]
             ])
print('Местоположение')
print(MP)
# Вычисление критерия согласия Местоположение
c=harmony(MP)
print ('Значение критерия согласия для матрицы 2-"Местоположение":',not_harm(c))
SED=result(MP)
print('Нормированные результаты сравнения по критерию 2-"Местоположение":', SED)


wait = input("Нажать ENTER для продолжения...")

# Характеристика жилого дома
kv_lesnay=float(6)
kv_zvezdnay = float(7)
kv_nevskiy = float(2)
kv_bogat = float(9)
kv_komenda = float(7)
kv_lagoj = float(3)

HG = np.mat([[kv_lesnay/kv_lesnay, kv_lesnay/kv_zvezdnay, kv_lesnay/kv_nevskiy, kv_lesnay/kv_bogat, kv_lesnay/kv_komenda,kv_lesnay/kv_lagoj ],
             [kv_zvezdnay/kv_lesnay, kv_zvezdnay/kv_zvezdnay, kv_zvezdnay/kv_nevskiy, kv_zvezdnay/kv_bogat, kv_zvezdnay/kv_komenda, kv_zvezdnay/kv_lagoj ],
             [kv_nevskiy/kv_lesnay, kv_nevskiy/kv_zvezdnay, kv_nevskiy/kv_nevskiy, kv_nevskiy/kv_bogat, kv_nevskiy/kv_komenda, kv_nevskiy/kv_lagoj],
             [kv_bogat/kv_lesnay,kv_bogat/kv_zvezdnay,kv_bogat/kv_nevskiy,kv_bogat/kv_bogat,kv_bogat/kv_komenda,kv_bogat/kv_lagoj],
             [kv_komenda/kv_lesnay,kv_komenda/kv_zvezdnay,kv_komenda/kv_nevskiy,kv_komenda/kv_bogat,kv_komenda/kv_komenda,kv_komenda/kv_lagoj],
             [kv_lagoj/kv_lesnay,kv_lagoj/kv_zvezdnay,kv_lagoj/kv_nevskiy,kv_lagoj/kv_bogat,kv_lagoj/kv_komenda,kv_lagoj/kv_lagoj]
             ])

print('Характеристика жилого дома')
print(HG)

# Вычисление критерия согласия
c=harmony(HG)
print ('Значения критерия согласия для матрицы 3-"Характеристика жилого дома" :', not_harm(c))
SCH=result(HG)
print('Нормированные результаты сравнения по критерию 3-"Характеристика жилого дома":', SCH)

wait = input("Нажать ENTER для продолжения...")

# Характеристика оцениваемой квартиры
kv_lesnay=float(4)
kv_zvezdnay = float(7)
kv_nevskiy = float(8)
kv_bogat = float(5)
kv_komenda = float(5)
kv_lagoj = float(6)

HK = np.mat([[kv_lesnay/kv_lesnay, kv_lesnay/kv_zvezdnay, kv_lesnay/kv_nevskiy, kv_lesnay/kv_bogat, kv_lesnay/kv_komenda,kv_lesnay/kv_lagoj ],
             [kv_zvezdnay/kv_lesnay, kv_zvezdnay/kv_zvezdnay, kv_zvezdnay/kv_nevskiy, kv_zvezdnay/kv_bogat, kv_zvezdnay/kv_komenda, kv_zvezdnay/kv_lagoj ],
             [kv_nevskiy/kv_lesnay, kv_nevskiy/kv_zvezdnay, kv_nevskiy/kv_nevskiy, kv_nevskiy/kv_bogat, kv_nevskiy/kv_komenda, kv_nevskiy/kv_lagoj],
             [kv_bogat/kv_lesnay,kv_bogat/kv_zvezdnay,kv_bogat/kv_nevskiy,kv_bogat/kv_bogat,kv_bogat/kv_komenda,kv_bogat/kv_lagoj],
             [kv_komenda/kv_lesnay,kv_komenda/kv_zvezdnay,kv_komenda/kv_nevskiy,kv_komenda/kv_bogat,kv_komenda/kv_komenda,kv_komenda/kv_lagoj],
             [kv_lagoj/kv_lesnay,kv_lagoj/kv_zvezdnay,kv_lagoj/kv_nevskiy,kv_lagoj/kv_bogat,kv_lagoj/kv_komenda,kv_lagoj/kv_lagoj]
             ])

print('Характеристика оцениваемой квартиры')
print(HK)

# Вычисление собственных значений матрицы и критерия согласия
c=harmony(HK)
print ('Значение критерия согласия для матрицы 4-"Характеристика оцениваемой квартиры" :', not_harm(c))
SAGE=result(HK)
print('Нормированные результаты сравнения по критерию 4-"Характеристика оцениваемой квартиры":', SAGE)

wait = input("Нажать ENTER для продолжения...")


# Получение итоговой оценки
N=len(alt1)
EV=np.zeros(N)
for k in range(N):
    EV[k]=CN[0]*SED[k]+CN[1]*SCH[k]+CN[2]*SAGE[k]
print('МАИ Оценки')
print(EV)
max = EV[0]
pos = 0
for i in range(len(EV)):
    if EV[i]>max: max=EV[i];pos=i
print ("max=",alt1[pos])


#МАИ+
Matrix_cr = CN
Matrix_mp = SED
Matrix_hd = SCH
Matrix_hk = SAGE

mp_norm = parn_sr(Matrix_mp)
hd_norm =parn_sr(Matrix_hd)
hk_norm =parn_sr(Matrix_hk)


print("\nСвертка частных оценок (Нормализованная матрица) Местоположение : ")
print(mp_norm)
wait = input("Нажать ENTER для продолжения...")


print("\nСвертка частных оценок (Нормализованная матрица) Характеристика жилого дома : ")
print(hd_norm)
wait = input("Нажать ENTER для продолжения...")

print("\nСвертка частных оценок (Нормализованная матрица) Характеристика оцениваемой квартиры : ")
print(hk_norm)
wait = input("Нажать ENTER для продолжения...")


SvOC = svertka_oc(mp_norm, hd_norm, hk_norm, CN)
print("\nПолучение сверток частных оценок в каждой паре по КРИТЕРИЯМ : ")
print(SvOC)

print("\nНормализация матрицы частных оценок : ")
NormSvOC =norm_svertka_oc(SvOC)
print(NormSvOC)

print("\nСумма по первым стобцам : ")
summ = summ_one_st(NormSvOC,len(alt1))
print(summ)

print("\nИтоговая Нормализация : ")
norm_summ = norm_summ(summ)
print(norm_summ)


# Получение итоговой оценки МАИ
N=len(alt1)
EV=np.zeros(N)
for k in range(N):
    EV[k]=CN[0]*SED[k]+CN[1]*SCH[k]+CN[2]*SAGE[k]
print('\nМАИ Оценки')
print(EV)
max = EV[0]
pos = 0
for i in range(len(EV)):
    if EV[i]>max: max=EV[i];pos=i
print ("max=",alt1[pos])


# Получение итоговой оценки МАИ+
NN=len(alt1)
RRES=np.zeros(NN)
for kk in range(NN):
    RRES[kk]= norm_summ[kk]
print('\nМАИ+ Оценки')
print(RRES)
max = RRES[0]
poss = 0
for ii in range(len(RRES)):
    if RRES[ii]>max: max=RRES[ii];poss=ii
print ("max=",alt1[poss])