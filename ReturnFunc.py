# -*- coding: utf-8 -*-
'''
Created on 2019年6月27日

@author: XPF
'''
from pip._vendor.progress import counter

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

#利用闭包返回一个计数器函数，每次调用它返回递增整数：
def createCounter():
    l = [0]
    def counter():
        l[0] = l[0]+1
        return l[0]
    return counter

def test(l):
    def counter():
        l[0] += 1
        return l[0]
    return counter

def createCounter1():
    def f(j):
        def g():
            return j
        return g
    return f


if __name__ == '__main__':
    f = lazy_sum(1,3,5,7,9)
    print(f)
    print(f())
    
    l = [1]
    counterA = createCounter()
    print(counterA(), counterA(), counterA(), counterA(), counterA())
    
    counterB = createCounter1()
    #print(counterB(1), counterB(1), counterB(1), counterB(1))
    counterB1 = counterB(1)
    print(counterB1())
    
    counterB1 = counterB(2)
    print(counterB1())
    
    counterB1 = counterB(3)
    print(counterB1())
    
    counterB1 = counterB(4)
    print(counterB1())
    
    counterB1 = counterB(5)
    print(counterB1())
    
    
    pass