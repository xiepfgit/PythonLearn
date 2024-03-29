# -*- coding: utf-8 -*-
'''
Created on 2019��6��13��

@author: XPF
'''
from _functools import reduce
from getpass import fallback_getpass

def FSquare(x, y):
    return x*y

def FAdd(x, y):
    return x + y

def ChangeStr(s):
    str1 = ''
    
    for i, sI in enumerate(s):
        if i == 0:
            str1 += sI.upper()
        else:
            str1 += sI.lower()
    return str1
    
def normalize(name):
    return name[0].upper() + name[1:].lower()

def FProd(L):
    return reduce(FSquare, L)
    
def FIs_Odd(n):
    return n % 2 == 1    
    
#移除空字符串
def not_empty(s):
    return s and s.strip()

#无限序列生成器
def _odd_iter():
    n = 1
    while True:
        n += 1
        yield n

#求素数
def _not_divisible(n):
    return lambda x : x % n > 0
   
#定义一个生成器，不断返回下一个素数        
def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)

def is_palindrome(n):
    s1 = str(n)
    length = len(s1)
    half = (length//2)+1
    for i, sItem in enumerate(s1):
        if s1[i] != s1[length-i-1]:
            return False
    return True

def by_name(t):
    s = str(t)
    return s.upper()
  
def by_score(t):
    l = list(t)
    return l[1]
    
if __name__ == '__main__':
    l = [1,2,3,4,5]
    l[0] = 0
    #print(list(map(FSquare, l, 2)))
    
    s = ['1', '2']
    s[0] = '2'
    print(s)
    
    name = ['adam', 'LISA', 'barT']
    #枚举字符串实现
    print(list(map(ChangeStr, name)))
    
    #切片实现
    print(list(map(normalize, name)))
    
        
    #reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
    print(reduce(FAdd, l))
    
    print(FProd([1,3,5,7,9]))
    
    #Filter
    print(list(filter(FIs_Odd, l)))
    
    
    l1 = ['A', '   ', 'B ', None, ' c', '']
    print(list(filter(not_empty, l1)))
    #用filter求素数
    
    l2 = list(range(10000))
    l2 = l2[2:]
    #print(l2)
    
    #由于primes()也是一个无限序列，所以调用时需要设置一个退出循环的条件：
    for i in primes():
        if i<1000:
            print(i)
        else:
            break

    
    output = filter(is_palindrome, range(0, 1000))
    print('1~1000:', list(output))
    
    #sorted排序
    L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
    print(sorted(L, key=by_name))
    
    print(sorted(L, key = by_score))
    
    pass

