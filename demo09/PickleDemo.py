try:
    import cPickle as pickle
except ImportError:
    import pickle

f = open('dump.txt', 'wb')
d = dict(name='Bob', age = 20, score = 88)
pickle.dump(d, f)
f.close();