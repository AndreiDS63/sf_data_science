from math import nan
import numpy as np

def arr_ations():
    arr = np.arange(8)
    print(arr)
    arr.shape = (2, 4)
    print(arr)

    # Чтобы оставить исходный массив без изменений
    arr = np.arange(8)
    arr_new = arr.reshape((2, 4))
    print(arr_new)

    # order задаёт принцип, по которому элементы заполняют массив новой формы
    # order='C' (по умолчанию), массив заполняется по строкам, как в примере выше
    # order='F' массив заполняется числами по столбцам
    arr = np.arange(8)
    arr_new = arr.reshape((2, 4), order='F')
    print(arr_new)


    # Транспонирование
    arr = np.arange(8)
    arr.shape = (2, 4)
    print(arr)

    arr_trans = arr.transpose()
    print(arr_trans)

    arr = np.arange(3)
    print(arr)
    print(arr.shape)

    arr_trans = arr.transpose()
    print(arr_trans)
    print(arr_trans.shape)
# arr_ations()


def arr_cuts():
    # one dimension arrays
    arr = np.linspace(1, 2, 6)
    print(arr)
    print(arr[2])
    
    print(arr[2:4])
    
    print(arr[::-1])
    
    # multi dimensions arrays
    nd_array = np.linspace(0, 6, 12, endpoint=False).reshape((3, 4))
    print(nd_array)
    
    # старая версия
    print(nd_array[1][2])
    
    # новая версия
    print(nd_array[1, 2])
    
    # получить все элементы из колонки 3 для первых 2х строк
    print(nd_array[:2, 3])
    
    # применить срез и к строкам и к столбцам
    print(nd_array[1:, 2:4])
    
    # получаем последнюю ось (в данном случае все столбцы)
    print(nd_array[:2])
# arr_cuts()


def sort_arrs():
    # case 1: sort() - function
    arr = np.array([23,12,45,12,23,4,15,3])
    print(arr)
    print()
    
    arr_new = np.sort(arr)
    print(arr_new)
    print()
    
    # case 2: сортирует исходный массив и возвращает None
    print('Case 2:')
    arr = np.array([23,12,45,12,23,4,15,3])
    print(arr.sort())
    print()
    print(arr)
# sort_arrs()


def missed_data():
    data = np.array([4, 9, -4, 3])
    roots = np.sqrt(data)
    print(roots)
    print()
    
    print(sum(roots))
    print()
    
    # узнаем где стоят nan
    print(np.isnan(roots))
    print()
    
    # извлекаем элементы из массива roots, на месте которых стоит nan
    print(roots[np.isnan(roots)])
    print()
    
    # этим элемента можем присвоить новые значения, например 0
    roots[np.isnan(roots)] = 0
    print(roots)
    print(sum(roots))
# missed_data()

