# 1. Python-9

## Оглавление 
[Модуль Collections. Counter и defaultdict](#модуль-collections-counter-и-defaultdict)  
    [Counter](#counter)

### Модуль Collections. Counter и defaultdict
В этом юните вы узнаете, как подсчитывать элементы в списке с помощью объекта Counter и создавать словарь с заданным по умолчанию объектом для упрощения написания кода.  

#### COUNTER
Предназначен для решения часто возникающей задачи по подсчёту различных элементов  
`from collections import Counter`  
`c = Counter(lst)`  
`c['elem']` - узнать сколько раз встретился конкретный элемент  
`sum(c.values())` - узнать сумму всех значений  
`Counter(lst1) + Counter(lst2)`  
`Counter(lst1).substract(Counter(lst2))`  
`print(*Counter(lst1).elements())` - список всех элементов  
`print(list(Counter(lst1)))` - список уникальных элементов  
`print(dict(Counter(lst1)))` - превратить Counter в обычный словарь  
`print(Counter(lst).most_common())` - список кортежей  
`print(Counter(lst).most_common(2))` - список из 2х кортежей  
`Counter(lst).clear()` - обнулить счетчик  

**DEFAULTDICT**  
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


:arrow_up:[к оглавлению](#оглавление)