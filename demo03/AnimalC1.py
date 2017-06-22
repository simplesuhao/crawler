#!user/bin/env python
# -*- coding: utf-8 -*-
' a test module '
'''此例为Animal的变种'''
class Animal(object):
    def run(self):
        print 'Animal is running'

'''子类增加方法'''
class Dog(Animal):
    def run(self):
        print 'Dog is running'
    def eat(self):
        print 'Dog is eating'
class Cat(Animal):
    def run(self):
        print 'Cat is running'

'''此时运行run方法，可以看到父类でrun方法被子类覆盖了'''
dog = Dog()
dog.run()
cat = Cat()
cat.run()

'''判断是否某个类型可以用isinstance()
通过下列的方法可以看到，继承而来的dog既是dog又是
animal，但animal不一定是dog'''
print isinstance(dog, Animal)
print isinstance(dog, Dog)
b = Animal()
print isinstance(b, Dog)