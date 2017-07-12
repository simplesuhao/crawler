try:
    import cPickle as pickle
except ImportError:
    import pickle
f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close()
print d