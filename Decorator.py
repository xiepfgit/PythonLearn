# -*- coding: utf-8 -*-


'''
Created on 2019��7��8��

@author: XPF

装饰器

'''

def now():
    print('2019-07-08')

def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def newNow():
    print('20190708')

#需要把原始函数的__name__等属性复制到wrapper()函数中，
#否则，有些依赖函数签名的代码执行就会出错
import functools

def log1(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' %(text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
        
@log1('execute')
def newNow1():
    print('20190708')
        

#pratice        
import time, functools
def metric(fn):
    print('%s executed in %s ms' % (fn.__name__, 06.50))
    return fn

@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z


if __name__ == '__main__':
    f = now
    print(f.__name__)
    
    newNow()
    
    newNow1()
    
    f = fast(11, 22)
    s = slow(11, 22, 33)
    
    print(f)
    print(s)
    
    pass