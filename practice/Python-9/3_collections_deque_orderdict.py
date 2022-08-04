def ord_dict_studing():
    data = [('Ivan', 19),('Mark', 25),('Andrey', 23),
            ('Maria', 20)
            ]
    client_ages = dict(data)
    print(client_ages)


    from collections import OrderedDict
    data = [('Ivan', 19),('Mark', 25),('Andrey', 23),
            ('Maria', 20)
            ]
    ordered_client_ages = OrderedDict(data)
    print(ordered_client_ages)

    # Сортируем по второму значению из кортежа, то есть по возрасту
    ordered_client_ages = OrderedDict(sorted(data, key=lambda x: x[1]))
    print(ordered_client_ages)

    ordered_client_ages['Nik'] = 18
    print(ordered_client_ages)

    del ordered_client_ages['Andrey']
    print(ordered_client_ages)

    ordered_client_ages['Andrey'] = 23
    print(ordered_client_ages)
    

from collections import deque
dq = deque()
print(dq)