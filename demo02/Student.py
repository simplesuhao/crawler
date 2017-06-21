#!user/bin/env python
# -*- coding: utf-8 -*-
' a test module '
class Student(object):
    ''' init方法的第一个参数永远是self'''
    def __init__(self, name, score):
        self.name = name
        self.score = score

bart = Student('Bart Simpson', 59)
print bart
print Student

print bart.score