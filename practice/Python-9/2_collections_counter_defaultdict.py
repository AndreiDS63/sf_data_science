from collections import Counter

cars = ['red', 'blue', 'black', 
        'black', 'black', 'red', 
        'blue', 'red', 'white'
        ]

# c = Counter()
# for car in cars:
#     c[car] += 1
 
# print(c)

c = Counter(cars)
print(c)
print(c['black'])
print(c['purple'])

# сумма всех значений в объекте
print(sum(c.values()))
print(c.values())


cars_moscow = ['black', 'black', 'white', 
               'black', 'black', 'white', 
               'yellow', 'yellow', 'yellow'
               ]

cars_spb = ['red', 'black', 'black', 
            'white', 'white', 'yellow', 
            'yellow', 'red', 'white'
            ]

counter_moscow = Counter(cars_moscow)
counter_spb = Counter(cars_spb)

print(f'counter_moscow: {counter_moscow}')
print(f'counter_spb: {counter_spb}')

# summ of counters
print(counter_moscow + counter_spb)

# difference of counters
counter_moscow.subtract(counter_spb)
print(counter_moscow)

# Пересоздаём счётчики, потому что объект counter_moscow поменял свои значения
# после функции subtract.
counter_moscow = Counter(cars_moscow)
counter_spb = Counter(cars_spb)
 
print(counter_moscow - counter_spb)
# Counter({'black': 2, 'yellow': 1})

print(*counter_moscow.elements())
print(list(counter_moscow))
print(dict(counter_moscow))
print(counter_moscow.most_common())
counter_moscow.clear()
print(counter_moscow)