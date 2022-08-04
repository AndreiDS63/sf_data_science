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
from pydoc import cli
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