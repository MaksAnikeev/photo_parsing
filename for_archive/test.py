"""ООП пространство имен"""

# Программист: использовать локальную переменную функции на уровне кода
# def printing():
#     global a
#     a = 3 + 5
#
# printing()
# print(a)

# альтернатива: использовать return

# Программист: использовать переменную с одним именем, но разными значениями на разных уровнях выполнения кода
# (на уровне внешней/включающей функции и на уровне всего кода)
# def scope_test():
#     def do_nonlocal():
#         nonlocal spam
#         spam = "nonlocal spam"
#
#     def do_global():
#         global spam
#         spam = "global spam"
#
#     spam = "test spam"
#     do_nonlocal()
#     print("After nonlocal assignment:", spam)
#     do_global()
#     print("After global assignment:", spam)
#
# scope_test()
#
# print("In global scope:", spam)

# Программист: при работе с асинхронными операциями сохранять информацию, чтобы затем использовать её в разных частях приложения
# import contextvars
# import asyncio
#
# user_var = contextvars.ContextVar('user')
#
# async def greet():
#     user = user_var.get()
#     print(f'Hello, {user}!')
#
#
# async def main():
#     user_var.set('Alice')
#     await greet()
#
#     user_var.set('Bob')
#     await greet()
#
# asyncio.run(main())
#
# Альтернативные решение - использовать глобальные переменные или создать класс и объявить объект класса на верхнем уровне кода


# var = 100  # A global variable
# def func():
#     global var
#     print(var)  # Reference the global variable, var
#     var = 200   # Define a new local variable using the same name, var
# func()
# func()

# Передать аргумент в функцию, а результат вывести return

# Сложность отладки: практически любой оператор в программе может изменить значение глобального имени.
# Трудно понять: вам необходимо знать обо всех операторах, которые обращаются к глобальным именам и изменяют их.
# Невозможно повторно использовать: код зависит от глобальных имен, специфичных для конкретной программы.





"""Классы"""

# Программист: получить доступ к приватным аргументам  и методам класса
# class Phone:
#     username = "Kate"                # public variable
#     __serial_number = "11.22.33"     # private variable
#     __how_many_times_turned_on = 0   # private variable
#
#     def call(self):                  # public method
#         print( "Ring-ring!" )
#
#     def __turn_on(self):             # private method
#         self.__how_many_times_turned_on += 1
#         print( "Times was turned on: ", self.__how_many_times_turned_on )
#
# my_phone = Phone()
#
# my_phone._Phone__turn_on()
# print( "New serial number is ", my_phone._Phone__serial_number )
# my_phone._Phone__serial_number = "44.55.66"
# my_phone._Phone__turn_on()
# print( "New serial number is ", my_phone._Phone__serial_number )
#
# input( "Press Enter to exit" )


# Программист: использовать данные в разной части программы, аналог redis
# class User:
#     def __init__(self, name):
#         self.name = name
#         self.number = int
#
# def print_number():
#     if user.number == 4:
#         print(f'Bingo {user.name}')
#     else:
#         print(user.number)
#
# user = User('Maks')
#
# while user.number != 4:
#     number = int(input('Введите число'))
#     user.number = number
#     print_number()


# Программист: создавать объекты, схожие по параметрам и не описывая каждый раз при создании их свойств и поведения.

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.position = 'programmer'
#         self.salary = 150000
#         self.company = 'Rambler'
#
#     def display_info(self):
#         print(f"Name: {self.name}  Age: {self.age}")
#
#     def annual_salary(self):
#         print(f"annual_salary {self.name}: {self.salary*12}")
#
#
# tom = Person("Tom", 37)
# bob = Person("Bob", 41)
# bob.salary = 200000
#
# bob.display_info()
# bob.annual_salary()
# tom.annual_salary()
# print(bob.company)

# >>> Name: Bob  Age: 41
# >>> annual_salary Bob: 2400000
# >>> annual_salary Tom: 1800000
# >>> Rambler


# Программист: изменять атрибут сразу для всех объектов класса
# class Test:
#     a = 1
#
#     @classmethod
#     def inc_a(cls):
#        cls.a += 1
#
# test1 = Test
# test2 = Test
# test3 = Test
#
# for i in range(4):
#     test3.inc_a()
#
# print(test1.a)
#
# # аналог
# a = 1
#
# def inc_a():
#     global a
#     a += 1



# Программист: как запретить изменять созданные объекты класса, и сравнивать между собой объекты класса
# from dataclasses import dataclass
# #
# @dataclass(order=True, frozen=True)
# class Test:
#     name: str
#     age: int
#
# max1 = Test('Max', 34)
# max1.age = 4
# max2 = Test('Max', 40)
#
# print(max1 > max2)
# >>>False




"""Методы классов"""

# Программист: расширить базовый класс новыми методами, переопределить метод базового класса
# Решение: использовать полиморфизм в наследовании классов
# from math import pi
#
#
# class Shape:
#     def __init__(self, name):
#         self.name = name
#
#     def fact(self):
#         return "I am a two-dimensional shape."
#
#     def __str__(self):
#         return self.name
#
# class Circle(Shape):
#     def __init__(self, radius):
#         super().__init__(self)
#         self.radius = radius
#
#     def area(self):
#         return pi*self.radius**2
#
#
# b = Circle(7)
# print(b.fact())
# print(b.area())
# >>> I am a two-dimensional shape.
# >>> 153.93804002589985

# Программист: переопределить метод и атрибуты базового класса
# Решение: использовать полиморфизм в наследовании классов и переопределение метода и атрибута класса
# class Parent:
#     def __init__(self):
#         self.town = 'Tomsk'
#         self.hair_color = "brown"
#         self.last_name = None
#
#     def message(self):
#         return f"Привет из {self.town}. Как дела?"
#
#     def fact(self):
#          return  f"У семейства {self.last_name} волосы {self.hair_color}"
#
#
# class Child(Parent):
#     def __init__(self, last_name):
#         super().__init__()
#         self.hair_color = "purple"
#         self.last_name = last_name
#
#     def message(self):
#         return f"Hello {self.last_name}. How qre you?"
#
# parent = Parent()
# child = Child('Петровы')
#
# print(parent.message())
# print(child.message())
# print(child.fact())
# >>> Привет из Tomsk. Как дела?
# >>> Hello Петровы. How qre you?
# >>> У семейства Петровы волосы purple


# Программист: расширить метод  класса
# Решение: использовать наследовании классов и расширение метода базового класса
# class Parent:
#     def __init__(self):
#         self.speaks = ["English"]
#
#     def fact(self):
#          return f"I am spiking {', '.join(self.speaks)}"
#
#
# class Child(Parent):
#     def __init__(self, new_language):
#         super().__init__()
#         self.speaks.append(new_language)
#
#     def add_language(self, new_language):
#         self.speaks.append(new_language)
#
# parent = Parent()
# child = Child("German")
# child.add_language('French')
#
# print(parent.speaks)
# print(parent.fact())
# print(child.speaks)
# print(child.fact())
#
# >>> ['English']
# >>> I am spiking English
# >>> ['English', 'German', 'French']
# >>> I am spiking English, German, French





# Программист: изменить представление атрибута класса без изменения самого атрибута
# Решение: использовать property()
# class Circle:
#     def __init__(self, radius):
#         self._radius = radius
#
#     def _get_diameter(self):
#         print("Get diameter")
#         return self._radius*2
#
#     def _set_radius(self, value):
#         print(f"Set new radius {value}")
#         self._radius = value
#
#     def _del_radius(self):
#         print("Delete radius")
#         del self._radius
#
#     radius = property(
#         fget=_get_diameter,
#         fset=_set_radius,
#         fdel=_del_radius,
#         doc="The radius property."
#     )
#
# circle = Circle(45)
# print(circle.radius)
# print(circle._radius)
# help(circle)

# class Circle:
#     def __init__(self, radius):
#         self._radius = radius
#
#     @property
#     def radius(self):
#         """Это документация"""
#         print("Get diameter")
#         return self._radius*2
#
#     @radius.setter
#     def radius(self, value):
#         print(f"Set new radius {value}")
#         self._radius = value
#
#     @radius.deleter
#     def radius(self):
#         print("Delete radius")
#         del self._radius
#
# circle = Circle(45)
# print(circle.radius)
# print(circle._radius)
#
# circle.radius = 55
# print(circle.radius)
# help(circle)


"""Это для себя"""
# class WriteCoordinateError(Exception):
#     pass
#
# class Point:
#     def __init__(self, x, y):
#         self._x = x
#         self._y = y
#
#     @property
#     def x(self):
#         return self._x
#
#     @x.setter
#     def x(self, value):
#         raise WriteCoordinateError("x coordinate is read-only")
#
#     @property
#     def y(self):
#         return self._y
#
#     @y.setter
#     def y(self, value):
#         raise WriteCoordinateError("y coordinate is read-only")
#
# point = Point(2, 33)
# print(point.y)
# point.y = 88

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     @property
#     def radius(self):
#         """Это документация"""
#         return self._radius
#
#     @radius.setter
#     def radius(self, value):
#         self._radius = float(value)
#
#     @radius.deleter
#     def radius(self):
#         print("Delete radius")
#         del self._radius
#
#     @property
#     def diameter(self):
#         print("Get diameter")
#         return self.radius * 2
#
#     @diameter.setter
#     def diameter(self, value):
#         print(f"Set diameter {value}")
#         self.radius = value / 2
#
#
# circle = Circle(45)
# print(circle.radius)
# print(circle.diameter)
#
# circle.diameter = 55
# print(circle.radius)
# print(circle.diameter)

from time import sleep

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._diameter = None
        self._radius = value

    @property
    def diameter(self):
        if self._diameter is None:
            print('Здесь задержка')
            self._diameter = self._radius * 2
        return self._diameter

circle = Circle(42.0)

print(circle.radius)
print(circle.diameter)
print(circle.diameter)

circle.radius = 100.0
print(circle.diameter)
print(circle.diameter)