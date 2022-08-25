import logging as logs

formt = ('%(asctime)s | %(message)s')
logs.basicConfig(filename='test2.log',level=logs.INFO, filemode='w',format=formt)
def devide(a,b):
    return a/b
print(devide(3,0))