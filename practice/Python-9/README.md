# 1. Python-9

## Оглавление 
* [Модуль Collections](#модуль-collections-counter-и-defaultdict)  
    + [Counter](#counter)
    + [Defaultdict](#defaultdict)
    + [Orderdict](#ordereddict)


### Модуль Collections
- как подсчитывать элементы в списке с помощью объекта Counter;  
- как создавать словарь с заданным по умолчанию объектом для упрощения написания кода;  
- как создавать объекты deque и OrderedDict;  
- как применять возможности очереди и стека на практике;  
-  как определять ситуации, в которых необходимо использовать новые изученные объекты вместо привычных list и dict.


#### COUNTER
Предназначен для решения часто возникающей задачи по подсчёту различных элементов  

№ п/п |код     | Описание
:----:|:------:|:----------:
1     |`from collections import Counter`|
2     |`c = Counter(lst)`|узнать сколько раз встретился конкретный элемент
3     |`sum(c.values())`|узнать сумму всех значений
4     |`Counter(lst1) + Counter(lst2)`| 
5     |`Counter(lst1).substract(Counter(lst2))`| 
6     |`print(*Counter(lst1).elements())`|список всех элементов
7     |`print(list(Counter(lst1)))`|список уникальных элементов 
8     |`print(dict(Counter(lst1)))`|превратить Counter в обычный словарь
9     |`print(Counter(lst).most_common())`|список кортежей
10     |`print(Counter(lst).most_common(2))`|список из 2х кортежей
11     |`Counter(lst).clear()`|обнулить счетчик

:arrow_up:[К оглавлению](#оглавление)


#### DEFAULTDICT
Позволяет задавать тот тип данных, который хранится в словаре по умолчанию. Бывает удобно в том случае, если приходится заполнять одну и ту же структуру данных, экземпляр которой должен храниться по каждому ключу в словаре.  

`from collections import defaultdict`  
`groups = defaultdict(list)` - в скобках передается указатель на класс объекта  

```
for student, group in students:  
    groups[group].append(student)  
print(groups)  
```  

`print(groups[3])` - обращение по ключу  
* обращение по несуществующему ключу возвращает пустой элемент, и в словаре создастся элемент с этим ключом с пустым значением  

:arrow_up:[К оглавлению](#оглавление)


#### ORDEREDDICT
Специальный словарь, который гарантирует сохранение ключей в порядке их добавления

`from collections import OrderedDict`  
`ordered_client_ages = OrderedDict(data)`  
```
# Сортируем по второму значению из кортежа, то есть по возрасту  
ordered_client_ages = OrderedDict(sorted(data, key=lambda x: x[1]))
```
* если добавить новый элемент в словарь - новая запись окажется в конце  
* до версии 3.7 не гарантируется сохранение порядка ключей в словаре
* узнать версию Python:  
```
import sys
print(sys.version)
```

:arrow_up:[К оглавлению](#оглавление)