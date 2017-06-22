#!user/bin/env python
# -*- coding: utf-8 -*-
' a test module '
'''多态的好处'''
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

def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal())
run_twice(Dog())
run_twice(Cat())