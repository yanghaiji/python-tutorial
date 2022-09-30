#!/usr/bin/env python
# coding=utf-8

"""
<p>

</p>
@author: hai ji
@file: classes.py
@date: 2022/9/22 
"""


class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart


x = Complex(3.0, -4.5)
print(x.i)
print(x.r)


class Animal:
    def __init__(self, name):
        self.name = name

    def hi(self):
        print('Hello, I am %s.' % self.name)


# class Dog():
#     def __init__(self, name):
#         self.name = name
#     def hi(self):
#         print('Wang Wang.., I am %s. ' % self.name)


# class Dog(Animal):
#
#     def hi(self):
#         print('Wang Wang.., I am %s. ' % self.name)


# Dog 类是从 Animal 类继承而来的，Dog 类自动获得了 Animal 类的所有数据和方法，而且还可以对从父类继承来的方法进行修改，调用的方式是一样的：

# animal = Animal('animal')
# animal.hi()
# dog = Dog('dog')
# dog.hi()


class Dog(Animal):
    def hi(self):
        print('Wang Wang.., I am %s. ' % self.name)

    def run(self):
        print('I am running!')


dog = Dog('dog')
dog.hi()
dog.run()


class Animal():
    def __init__(self, name):
        self.name = name

    def hi(self):
        print(f'Hello, I am {self.name}.')


class Dog(Animal):
    def hi(self):
        print(f'WangWang.., I am {self.name}.')


class Cat(Animal):
    def hi(self):
        print(f'MiaoMiao.., I am {self.name}')


def hello(animal):
    animal.hi()


dog = Dog('dog')
hello(dog)
cat = Cat('cat')
hello(cat)


class Fib():
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a


fib = Fib()
for i in fib:
    if i > 10:
        break
    print(i)  # 1, 1, 2, 3, 5, 8


class Animal():
    def __init__(self, name):
        self.__name = name

    def hi(self):
        print(f'Hello, I am self.__name.')


animal = Animal('a1')
# animal.__name  # error
