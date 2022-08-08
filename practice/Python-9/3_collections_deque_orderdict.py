import collections


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
    
    
def deque_studing():
    
    from collections import deque
    dq = deque()
    print(dq)


    clients = deque()
    clients.append('Ivanov')
    clients.append('Petrov')
    clients.append('Smirnov')
    clients.append('Tikhonova')
    print(clients)

    print(clients[2])

    first_client = clients.popleft()
    second_client = clients.popleft()

    print(f'First client: {first_client}')
    print(f'Second client: {second_client}')
    print(clients)

    clients.appendleft('VIP-client')
    print(clients)

    tired_client = clients.pop()
    print(tired_client, 'left the queue')
    print(clients)

    clients = deque(['Ivanov', 'Petrov', 'Smirnov', 
                    'Tikhonova'
                    ])
    print(clients)
    del clients[2]
    print(clients)


    shop = deque([1, 2, 3, 4, 5])
    print(shop)
    shop.extendleft([11, 12, 13, 14, 15, 16, 17])
    print(shop)

    limited = deque(maxlen=3)
    print(limited)

    limited_from_list = deque([1,3,4,5,6,7], maxlen=3)
    print(limited_from_list)

    limited.extend([1,2,3])
    print(limited)

    print(limited.append(8))

    print(limited)

    temps = [20.6, 19.4, 19.0, 19.0, 22.1,
            22.5, 22.8, 24.1, 25.6, 27.0,
            27.0, 25.6, 26.8, 27.3, 22.5,
            25.4, 24.4, 23.7, 23.6, 22.6,
            20.4, 17.9, 17.3, 17.3, 18.1,
            20.1, 22.2, 19.8, 21.3, 21.3,
            21.9
            ]

    days = deque(maxlen=7)

    for temp in temps:
        days.append(temp)
        if len(days) == days.maxlen:
            print(round(sum(days) / len(days), 2), end='; ')
    print('')


    dq = deque([1,2,3,4,5])
    print(dq)

    dq.reverse()
    print(dq)


    dq = deque([1,2,3,4,5])
    print(dq)

    dq.rotate(-2)
    print(dq)


def task_3_2():
    """Необходимо напечатать словарь, в котором ключи — годы, 
    а значения — показатели температуры. 
    Ключи необходимо отсортировать в порядке убывания 
    соответствующих им температур.
    """
    
    temps = [('2000', -4.4), ('2001', -2.5), ('2002', -4.4), ('2003', -9.5),
        ('2004', -8.2), ('2005', -1.6), ('2006', -5.9), ('2007', -2.4),
        ('2008', -1.7), ('2009', -3.5), ('2010', -12.1), ('2011', -5.8),
        ('2012', -4.9), ('2013', -6.1), ('2014', -6.9), ('2015', -2.7),
        ('2016', -11.2), ('2017', -3.9), ('2018', -2.9), ('2019', -6.5),
        ('2020', 1.5)
        ]
    
    from collections import OrderedDict
    ordered_temps_dict = OrderedDict(sorted(temps, key=lambda x:x[1], reverse=True))
    print(ordered_temps_dict)
    
    
# task_3_2()


