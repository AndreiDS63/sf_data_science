# 1. Python-9

## Оглавление 
[Модуль Collections. Counter и defaultdict](#модуль-collections-counter-и-defaultdict)

### Модуль Collections. Counter и defaultdict
В этом юните вы узнаете, как подсчитывать элементы в списке с помощью объекта Counter и создавать словарь с заданным по умолчанию объектом для упрощения написания кода.  

**Counter**  
Предназначен для решения часто возникающей задачи по подсчёту различных элементов  
* from collections import Counter  
* c = Counter(lst)  
* c['elem'] - узнать сколько раз встретился конкретный элемент  
* sum(c.values()) - узнать сумму всех значений  
* Counter(lst1) + Counter(lst2)  
* Counter(lst1).substract(Counter(lst2))  
* print(*Counter(lst1).elements()) - список всех элементов  
* print(list(Counter(lst1))) - список уникальных элементов  
* print(dict(Counter(lst1))) - превратить Counter в обычный словарь  
* print(Counter(lst).most_common()) - список кортежей  
* print(Counter(lst).most_common(2)) - список из 2х кортежей  
* Counter(lst).clear() - обнулить счетчик


:arrow_up:[к оглавлению](#оглавление)