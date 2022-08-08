import numpy as np


def time_check():
    import time
    start_time = time.time()
    print(f'start_time: {start_time}')
    lst = [i for i in range(10000000)]
    num = lst[9999999]
    end_time = time.time()
    print(f'end_time: {end_time}')
    delta = end_time - start_time
    print(f'delta: {delta} sec')
    
def arr_study():
    arr = np.array([1, 5, 2, 9, 10])
    print(arr)
    print(type(arr))

    nd_arr = np.array([
                [12, 45, 78],
                [34, 56, 13],
                [12, 98, 76]
                ])
    print(nd_arr)
    print(arr.dtype)
# arr_study()


def arr_prop_study_():
    arr = np.array([1, 5, 2, 9, 10], dtype=np.int16)

    nd_arr = np.array([
                [12, 45, 78],
                [34, 56, 13],
                [12, 98, 76]
                ])
    
    # узнать размерность массива
    print(arr.ndim)
    print(nd_arr.ndim)
    
    # узнать общее число элементов
    print(arr.size)
    print(nd_arr.size)
    
    #узнать форму или структуру массива
    print(arr.shape)
    print(nd_arr.shape)
    
    # сколько весит каждый элемент массива в байтах 
    print(arr.itemsize)
    print(nd_arr.itemsize)
    
    print(arr.dtype)
    print(nd_arr.dtype)
# arr_prop_study_()

def new_arrs_study():
    zeros_1d = np.zeros(5)
    print(zeros_1d)

    zeros_3d = np.zeros((5, 4, 3), dtype=np.float32)
    print(zeros_3d.shape)

    print(np.arange(5))

    print(np.arange(2.5, 5))

    print(np.arange(2.5, 5, 0.5))

    print(np.arange(2.5, 5, 0.5, dtype=np.float16))

    print(np.linspace(1, 2, 10))

    print(np.linspace(1, 2, 10, endpoint=False))

    arr, step = np.linspace(1, 2, 10, endpoint=True, retstep=True)
    print(step)

    arr, step = np.linspace(1, 2, 10, endpoint=False, retstep=True)
    print(step)

    arr, step = np.linspace(-6, 21, 60, endpoint=True, retstep=True)
    print(round(step, 2))

    arr, step = np.linspace(-6, 21, 60, endpoint=False, retstep=True)
    print(round(step, 2))
# new_arrs_study()