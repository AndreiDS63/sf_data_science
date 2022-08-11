import numpy as np

def float_gen():
    print(np.random.rand())
    print(np.random.rand() * 100)
    print()

    print(np.random.rand(5))
    print()

    print(np.random.rand(2, 3))
    print()

    # print(np.random.rand(2, 3, 4, 10, 12, 23))

    # если нужно принять кортеж без распаковки
    shape = (2, 3)
    print(np.random.sample(shape))

    print()
    print('np.random.uniform()')
    print(np.random.uniform())
    print()

    print('np.random.uniform(-30, 50)')
    print(np.random.uniform(-30, 50))
    print()

    print('np.random.uniform(-0.5, 0.75)')
    print(np.random.uniform(-0.5, 0.75))
    print()

    print('np.random.uniform(-0.5, 0.75, size=5))')
    print(np.random.uniform(-0.5, 0.75, size=5))
    print()

    print('np.random.uniform(-1000, 500, size=(2, 3))')
    print(np.random.uniform(-1000, 500, size=(2, 3)))
    print()
# float_gen()

def int_gen():
    print('np.random.randint(4, size=(2, 3))')
    print(np.random.randint(4, size=(2, 3)))
    print()
    
    print('np.random.randint(6, 12, size=(3, 3))')
    print(np.random.randint(6, 12, size=(3, 3)))
    print()
# int_gen()

def sample_gen():
    arr = np.arange(6)
    print('arr')
    print(arr)
    print()
    
    print('np.random.shuffle(arr)')
    print(np.random.shuffle(arr))
    print(arr)
    print()
    
    #чтобы получить новый перемешанный массив
    playlist = ["The Beatles", "Pink Floyd", "ACDC", "Deep Purple"]
    shuffled = np.random.permutation(playlist)
    print('shuffled')
    print(shuffled)
    print('playlist')
    print(playlist)
    print()
    
    #перемешать набор чисел
    print('np.random.permutation(10)')
    print(np.random.permutation(10))
    print()
    
    workers = ['Ivan', 'Nikita', 'Maria', 'John', 'Kate']
    choise = np.random.choice(workers, size=2, replace=False)
    print('choise')
    print(choise)
    print()
    
    # подбрасывание игральной кости
    choise = np.random.choice([1, 2, 3, 4, 5, 6], size=10)
    print('choise')
    print(choise)
# sample_gen()

def seed_gen():
    np.random.seed(23)
    print('np.random.randint(10, size=(3, 4))')
    print(np.random.randint(10, size=(3, 4)))
    print()
    
    np.random.seed(100)
    print('np.random.randint(10, size=3)')
    print(np.random.randint(10, size=3))
    print(np.random.randint(10, size=3))
    print(np.random.randint(10, size=3))
    print()
# seed_gen()
