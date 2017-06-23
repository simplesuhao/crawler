from types import MethodType
def set_age(self, age):
    self.age = age
def set_score(self, score):
    self.score = score

class Student(object):
    __slots__ = ('name', 'age', 'score')
    pass

s = Student()
s.name = 'wwa'
print s.name

s.age = 25
print s.age

s.score = 98
print s.score
