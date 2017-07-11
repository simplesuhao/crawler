try:
    f = open('C:\Users\Administrator\Desktop\ceshi.txt','r')
    print f.read()
finally:
    f.close()


with open('C:\Users\Administrator\Desktop\ceshi.txt','r') as f:
    print f.read()


with open('C:\Users\Administrator\Desktop\ceshi.txt','r') as f:
    for line in f.readlines():
        print line.strip()