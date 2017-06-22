#!user/bin/env python
# -*- coding: utf-8 -*-
' a test module '
class Student(object):
    '''init方法的第一个参数永远是self'''
    def __init__(self, name, score):
        '''add access restriction'''
        self.__name = name
        self.__score = score
    '''对数据进行封装'''
    def print_score(self):
        print '%s: %s' % (self.__name, self.__score)
    '''增加新的方法'''
    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >=60:
            return 'B'
        else:
            return 'C'
    '''增加get&set方法'''
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('Bad score')
bart = Student('vva', 89)
print bart.get_score()
bart.print_score()
print bart.get_grade()