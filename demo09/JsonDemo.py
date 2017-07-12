try:
    import cPickle as pickle
except ImportError:
    import pickle
import json

f = open('dump.txt','rb')
d = pickle.load(f)
j = json.dumps(d)
print j