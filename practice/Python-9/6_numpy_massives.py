from multiprocessing.spawn import import_main_path


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
    import numpy as np
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
    import numpy as np
    
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
arr_prop_study_()