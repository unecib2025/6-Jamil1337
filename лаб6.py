1.
#a = input()
#b = input()
#c =input()
#c=[]
#c.append(a)
#c.append(b)
#c.append(c)
#print(c)
2.
#c=['root','security']
#a=input()
#c.insert(0,a)
#print(c)
3.
#a=input('alice')
#c=['bob','charlie','alice']
#c.remove(a)
#print(c)
4.
#c =['Access granted','Login failed','Connection lost']
#c.pop()
#print(c)
5.
#a=['ok', 'error', 'ok', 'error', 'error']
#print(a.count('error'))
6.
#a=['Access ok', 'Breach detected', 'System reboot', 'Breach detected']
#print(a.index('Breach detected'))
7.
#a=[3, 1, 2, 3, 1, 2]
#a.sort()
#print(a)
8,
#a=['2025-10-01', '2025-10-02', '2025-10-03']
#a.reverse()
#print(a)
9.
#a=["alert", "spam", "login", "error", "spam", "alert"]
#a.remove('spam')
#a.remove('spam')
#a.append('END_LOG')
#a.reverse()
#print(a, 'alerts-',a.count('alerts'))
10.
#dex=['192.168.0.1', '192.168.0.3', '192.168.0.2 ' , '192.168.0.4', '192.168.0.5']
#a=input('Delete iP')
#dex.remove(a)
#c=input('Add new iP')
#dex.insert(2,c)
#dex.sort()
#print(dex)
11.
#c=['ok', 'fail', 'fail', 'ok', 'fail']
#f=c.count('fail')
#while 'fail' in c:
#    c.remove('fail')
#c.append("audit_completed" )
#c.reverse()
#print(f'Количество неудачных входов: {f}',f'Итоговый список: {c}',f'Первый индекс "ok": {c.index('ok')}', sep='\n')
1. #append() добовляет значение в конец списка, insert() добовляет значение на выбранный индекс тем самым сдивгая все значения на 1 вперед
2. #удаляет последнее значение в списке
3. #remove() удаляет только первое вхождение, удалить все значения элемента можно сделать при помощи цикла, как сделал я в 11 задании
4. #reverse() переворачивает список на месте, то есть меняет порядок элементов в обратный без создания нового списка
5. #count() считает кол во значений в списке, а index() показывает индекс первого вхождения элемента
6. #append() extend() insert() remove() pop() clear() reverse() sort() изменяют исходный список
   #a.copy() sorted(a) a.copy() и срезы возвращают новое значение , в основном все встроенные функции возвращают новое значение
7. #произойдет ошибка
8. #потому что она помогает быстрее выявлять закономерности и отклонения.