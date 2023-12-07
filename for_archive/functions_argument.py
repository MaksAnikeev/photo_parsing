# Проблема: передать в функцию произвольное количество аргументов.
# def cheeseshop(kind, *args, **kwargs):
#     print("-- У вас есть сыр", kind, "?")
#     print(f"-- К сожалению, {kind} сейчас нет")
#     for arg in args:
#         print(arg)
#     print("-" * 40)
#     for kw in kwargs:
#         print(kw, ":", kwargs[kw])
#
# cheeseshop("Бри", "Мне жаль",
#            "Мне, действительно, очень жаль",
#            продавец="Michael Palin",
#            клиент="John Cleese",
#            магазин="Cheese Shop Sketch")

# Проблема: передать позиционный и именнованный аргумент с одинаковым именем в функцию
# def foo(name, /, **kwds):
#     print(name)
#     print(kwds['name'])
#
# foo(1, name=2)

# Проблема: получить только 1 значение из нескольких возвращаемых значений из функции с помощью return
# def example(a):
#     b = a + 1
#     c = a + 2
#     d = b + c
#     e = a ** 2
#     return b, c, d, e
#
# print(example(2)[2])
#
# b, c, d, e = example(2)
# print(d)
#
# print(example(2)[2])

# Проблема: происходит ошибка при вызове функции когда путают местами позиционные аргументы
# def kwd_only_arg(*, a, b, c, d):
#     print(a)
#     print(b)
#     print(c)
#     print(d)
#
# kwd_only_arg(b=2,
#              a=1,
#              d=4,
#              c=3)

# Проблема: передать в функцию аргументы с помощью словаря словарь или списка
# def parrot(voltage, state='a stiff', action='voom'):
#     print("-- This parrot wouldn't", action, end=' ')
#     print("if you put", voltage, "volts through it.", end=' ')
#     print("E's", state, "!")
#
# d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
# parrot(**d)
#
# args = [3, 6]
# print(list(range(*args)))
# pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
#
# pairs.sort(key=lambda x: x[1])
# print(pairs)




# Проблема: понять являются ли для языка программирования одинаковыми значения, которые выглядят одинаково
# print('5')
# print(5)
# # >>> 5
# # >>> 5
#
# print(hash('5'))
# print(hash(5))
# >>> 8509471920655836434
# >>> 5

# Проблема: нужно узнать являются ли значения различных объектов (переменных, тьюплов) одинаковыми
# dict1 = {3: 'Maks', 2: "Den", 1: "Alex"}
# dict2 = {1: "Frend", 2: "alex", 3: "Alex"}
#
# name1 = dict1[1]
# name2 = dict2[2]
# name3 = dict2[3]
# name4 = name3
#
# print(hash(name1))
# print(hash(name2))
# print(hash(name4))
#
# # >>> 91405530151842685
# # >>> 6109903252685575157
# # >>> 91405530151842685
#
# tuple_a = (1, 2, 3)
# print(hash(tuple_a))
# tuple_b = (2, 3, 4)
# print(hash(tuple_b))
# tuple_c = (1, 2, 3)
# print(hash(tuple_c))
#
# # >>> 529344067295497451
# # >>> -3165226637586315787
# # >>> 529344067295497451

# # Проблема: проверить все ли элементы кортежа являются неизменяемыми (нет ли в элементе корьежа списка или словаря)
# tt = (1, 2, (30, 40))
# tl = (1, 2, [30, 40])
# def check_unmutable(object):
#     try:
#         hash(object)
#         print(True)
#     except TypeError:
#         print(False)
#
# check_unmutable(tt)
# # >>> True
# check_unmutable(tl)
# # >>> False

# TypeError: unhashable type: 'list'

# Программист: определить есть ли повторяющие элементы в списке
# list1 = [1, 4, 6, 3, 7, 4]
#
# print(len(set(list1)) == len(list1))
#
# print(5==5.0)

from string import punctuation
# punctuations = '.,;/'
# score = 0

# with open('test.txt', 'r', encoding="utf-8") as file_for_text:
#     text = file_for_text.read()
# for symbol in text:
#     if symbol in punctuation:
#         score += 1
# score = text.find('.')
# print(text.find(','))



# from collections import Counter
#
# arr = [3,4,3,2,3,2,3,3,9,10]
# print(Counter(arr))
#
# counted_arr = {}
# for a in arr:
#     if a not in counted_arr:
#         counted_arr[a] = 1
#     else:
#         counted_arr[a] += 1
# print(counted_arr)
# def is_immutable(obj):
#     try:
#         hash(obj)
#     except TypeError:
#         return False
#     return True
#
# class A:
#     pass
#
# a = A()
# a.x = 1
# print(a.x)
# # if is_immutable(a):
# #     print("Really?")
# print(is_immutable(a.x))













# Программист: добавлять элементы в тьюпл
# another_tuple = ([1], [4], [6])
# another_tuple[2].append(99)
# print(another_tuple)


# Программист: удалить элемент из списка во время итераций по списку OK
# list_1 = [1, 2, 3, 4, 5, 6]
# list_2 = [1, 2, 3, 4]
# list_3 = [1, 2, 3, 4]
#
# for num, item in enumerate(list_1, start=1):
#     print(list_1)
#     print(num)
#     if num%2 == 0:
#         list_1.remove(item)
#         num -= 1
#         list_1 = list_1[:num-1] + list_1[num:]
#
# for item in list_2[:]:
#     list_2.remove(item)
#
# for item in list_3.copy():
#     list_3.remove(item)
#
# print(list_1)
# [2, 4]
# print(list_2)
# []
# print(list_3)


# Программист: быстро создать список, например, чтобы посчитать сумму всех чисел в числе OK
# total = sum([int(digit) for digit in str(abs(6538964))])
# print(total)

# Программист: отсортировать разные данные в списке OK
# print(sorted(['A', 'h', 'b', 'd', 'C'], key=str.lower))


# Программист: не путаться в индексах при использования разных тьюплов с большим количеством элементов
# Другой способ создание класса
# from collections import namedtuple
# Car = namedtuple('Car', 'color, speed, type, mileage, model')
# Truck = namedtuple('Truck', 'speed, mileage, model, tonnage')
#
# car1 = Car('red', 240, 'sedan', 125, 'ford')
# car2 = Car('blue', 220, 'hatchback', 315, 'opel')
# truck1 = Truck(150, 180, 'kamaz', 25)
#
# print(car1.mileage < truck1.mileage)
# print(car2.mileage < truck1.mileage)

# Программист: не путаться в индексах при использования разных тьюплов с большим количеством элементов
# import json
# from collections import namedtuple
#
# Car = namedtuple('Car', 'color, speed, type, mileage, model')
#
# car1 = Car('red', 240, 'sedan', 125, 'ford')
#
# print(json.dumps(car1._asdict()))



# Перевести лист в именнованный кортеж
# from collections import namedtuple
#
# Car = namedtuple('Car', 'color, speed, type, mileage, model')
# car1 = ['red', 240, 'sedan', 125, 'ford']
# print(Car._make(car1))

# Расширить список OK
# list_1 = [1, 2, 3, 4]
# list_2 = [5, 6, 7]
# list_1.extend(list_2)
# print(list_1)


# Например:{(<x-coordinate>,<y-coordinate>): <indicating letter>}
# [[1,2012,5],[2,2012,6],...].
# {'1_2012':'5','2_2012':'50', ...}

# coordinates = {(3, 5): 'right_point',
#                (4, 6): 'left_point',
#                (0, 3): 'top_point',
#                (6, 6): 'bottom_point'}





# dict

# Программист: передать в HTML шаблон изменяемые данные
# во вьюхах джанго создаем список словарей с набором данных, а в HTML
# идем по этому списку и из словаря вытаскиваем нужные данные по ключам
# def index_page(request):
#     orders = Order.objects.filter(order_status='raw_order')
#     orders_params = [
#                 {
#                     'id': order.id,
#                     'firstname': order.firstname,
#                     'lastname': order.lastname,
#                     'phonenumber': order.phonenumber,
#                     'address': order.address,
#                     'delivered_at': order.delivered_at,
#                     'order_status': order.get_order_status_display(),
#                     'payment': order.get_method_payment_display(),
#                     'order_price': order.bunch.price,
#                     'bunch_name': order.bunch.name,
#                     'bunch_id': order.bunch.id,
#                     'comment': order.comment,
#                 }
#                 for order in orders]
#
#     context = {'order_params': orders_params}
#     return render(request, template_name='index.html', context=context)
#
# верстка
# {% for item in order_params %}
#       <tr>
#         <td>{{item.id}}</td>
#         <td>{{item.firstname}} {{item.lastname}}</td>
#         <td>{{item.phonenumber}}</td>
#         <td>{{item.address}}</td>
#         <td>{{item.delivered_at}}</td>
#         <td>{{item.order_status}}</td>
#         <td>{{item.payment}}</td>
#         <td>{{item.bunch_name}}</td>
#         <td>{{item.bunch_id}}</td>
#         <td>{{item.order_price}} руб.</td>
#         <td>{{item.comment}}</td>
#         <td><a href="{% url 'admin:flower_shop_order_change' object_id=item.id %}?next={{ request.get_full_path|urlencode }}">
#           Редактировать</a></td>

# можно использовать список, но тогда будешь четко привязан к месту элемента в списке и нужно помнить кажды индекс в списке

# Программист: передать данные в БД
# тспользуем post запрос со словарем данных, которые хотим передать
# url = "http://127.0.0.1:8000/api/favourites/add"
# payload = {
#     'user_tg_id': context.user_data["telegram_id"],
#     'recipe_name': recipe_name
# }
# response = requests.post(url, data=payload)
# response.raise_for_status()
#
# альтернатива использование get запросов с указанием передаваемых данных в составе url
# url = f"http://127.0.0.1:8000/api/users/{telegram_id}"
# response = requests.get(url)

# Программист: поменять местами ключи и значения в словаре
# использовать dict comprehensions
# def invert(d):
#     return {v: k for k, v in d.items()}
#
# d = {0 : 'A', 1 : 'B', 2 : 'C', 3 : 'D'}
# print(invert(d))

# set
#
# list_1 = [1, 2, 3, 1, 2]
# num_set = set(list_1)
# print(num_set)
# words = ['hello', 'daddy', 'hello', 'mum']
# print(set(words))


# пересечение множеств
# x = {1, 2, 3, 8, 9}
# y = {4, 3, 6}
#
# print(x & y)

# Программист: определить есть ли повторяющие элементы в списке

# list1 = [1, 4, 6, 3, 7, 4]
#
# def check_equal_elements(l):
#     return not len(set(l)) == len(l)
#
# print(check_equal_elements(list1))

# frozenset
# fs = frozenset([1, 2, 3, 4, 5])
# fs1 = fs.symmetric_difference(frozenset([1, 2, 10, 20]))
# print(fs1)
#
# lang_X = {'C++', 'Perl', 'PHP', 'Java', 'C#'}
# lang_Y = {'Python'}
# lang_Z = lang_X.union(lang_Y)
# print(lang_Z)






# Программист: дать свое описание возникающему исключению
# try:
#     f = 555/0
# except Exception as err:
#     print(f"У тебя ошибка {err}, тип ошибки {type(err)=}")
#     f = 0
#
# print(f)


# # Программист: поднять исключение и переделать одно исключение в другое
# def func():
#     raise ZeroDivisionError
#
# try:
#     func()
# except ZeroDivisionError:
#     raise RuntimeError('Failed to open database') from None

# # Программист: выполнить определенное действие, даже если поднято исключение (например для освобождения внешних ресурсов
# (таких как файлы или сетевые подключения) независимо от того, было ли использование ресурса успешным, пример удаление корутин в асинхронном пайтане)
# def divide(x, y):
#     try:
#         result = x / y
#         print("result is", result)
#     except ZeroDivisionError:
#         print("division by zero!")
#     finally:
#         print("executing finally clause")
#
# divide(2, 1)
# divide('2', '1')
# Решение альтернативное: везде написать print("executing finally clause") и сделать пустое except с этой фразой


# Программист: создать собственное исключение
# class MyCustomException(Exception):
#     def __init__(self, message, extra_info):
#         super().__init__(message)
#         self.extra_info = extra_info
#
#
# def divide_numbers(a, b):
#     if b == 10:
#         raise MyCustomException("На 10 надо делить в уме", {"a": a, "b": b})
#     return a / b
#
#
# try:
#     print(divide_numbers(345, 10))
# except MyCustomException as e:
#     print(f"Сообщение об ошибке: {e}")
#     print(f"Дополнительная информация: {e.extra_info}")
#
#
# a = input("Input positive integer: ")
#
# try:
#     a = int(a)
#     if a < 0:
#         raise MyCustomException("You give negative!", None)
# except ValueError:
#     print("Error type of value!")
# except MyCustomException as mr:
#     print(mr)
# else:
#     print(a)


# while True:
#     try:
#         print(";".join(str(1 / x) for x in range(int(input()), int(input()) + 1)))
#         break
#     except ZeroDivisionError:
#         print("Диапазон чисел содержит 0. Попробуйте еще раз")
#     except ValueError:
#         print("Введены НЕ числа. Попробуйте еще раз")

