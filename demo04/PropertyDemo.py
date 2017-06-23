class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be integer!')
        if value < 0 or value > 100:
            raise  ValueError('score must be 0 ~ 100!')
        self._score = value

if __name__ == '__main__':
    s = Student()
    s.score = 90
    print s.score