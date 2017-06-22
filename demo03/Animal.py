#!user/bin/env python
# -*- coding: utf-8 -*-
' a test module '
class Animal(object):
    def run(self):
        print 'Animal is running'

class Dog(Animal):
    pass
class Cat(Animal):
    pass

'''通过下面这些例子可以看到，
虽然Dog Cat方法中并没有runで方法
但是其依然可以调用并执行'''
dog = Dog()
dog.run()
cat = Cat()
cat.run()