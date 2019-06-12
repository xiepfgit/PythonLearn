# -*- coding: utf-8 -*-

'''
Created on 2019��6��10��

@author: XPF
'''
from collections import Iterable
from inspect import isgeneratorfunction

#去除两端的空格
def Trim(s):
    if s[0] == ' ':
        s = s[1:s.__len__()]
    nLength = len(s)
    if s[nLength-1] == ' ':
        s = s[0:nLength]
    return s

#斐波那契数列
def Fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b     #使用yield
        #print (b)
        a, b = b, a+b
        n = n+1
        
#杨辉三角
def Triangles(max):
    n1 = 0
    trianglesL = [1]
    
    while(n1 < max):
        yield trianglesL
        n1 += 1
        lSize = len(trianglesL)
        L = []
        for n, item in enumerate(trianglesL):
            if n == 0:
                continue
            else:
                L.append(trianglesL[n-1] + trianglesL[n])
        L.insert(0, 1)
        L.insert(len(L), 1)
        trianglesL = L
        
def NewTrianbles(max):
    N = [1]
    ii = 0
    while ii<max:
        ii += 1
        yield N
        N.append(0)
        N = [N[i-1] + N[i] for i in range(len(N))]
    

if __name__ == '__main__':
    #函数
    n1 = 255
    print(hex(n1))
    n2 = 1000
    print(hex(n2))
    #切片
    L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
    #取前三个元素0,1,2不包括第三个
    print(L[:3])
    #取1,2个元素
    print(L[1:3])
    #取倒数两个元素，不包括0
    print(L[-2:])
    
    #下面找不到元素：因为倒数的第一个元素的索引是-1
    print(L[-2:0])
    
    L = list(range(100))
    print(L)
    print(L[0:10])
    print(L[-10:])
    
    #前10个数每两个取一个
    print(L[:10:2])
    #所有数每五个取一个
    print(L[::5])
    
    s = '  abcd  '
    print(Trim(s))
    
    #迭代
    d = {'a':1, 'b':2, 'c':3}
    for value in d.values():
        print(value)
        
    for ch in 'ABCD':
        print(ch)
        
    print(isinstance('abc', Iterable))
    
    print(isinstance(123, Iterable))
    
    #实现下标循环
    for i , value in enumerate(['A', 'B', 'C']):
        print(i, value)
    
    for x, y in [(1,1), (2,4), (3,9)]:
        print(x,y)
    
    
    #列表生成表达式
    l1 = [x*x for x in range(1, 11)]
    print(l1)
    
    #加上判断
    l2 = [x*x for x in range(1,11) if x%2 == 0]
    print(l2)
    
    #多层循环
    l3 = [m+n for m in 'ABC' for n in 'XYZ']
    print(l3)
    
    #列表生成式也可以使用两个变量来生成list
    d = {'x':'A', 'y':'B', 'z':'C'}
    l4 = [k + '=' + v for k, v in d.items()]
    print(l4)
    
    #最后一个list中所有字符串变成小写：
    l5 = {'Hello', 'World', 'IBM', 'Apple'}
    print([s.lower() for s  in l5])
    
    
    #生成器generator 和上面的list区别也只是[] 和 ()的区别
    g = (x * x for x in range(10))
    for n in g:
        print(n)
    '''
            简单地讲，yield 的作用就是把一个函数变成一个 generator，带有 yield 的函数不再是一个普通函数，
    Python 解释器会将其视为一个 generator，调用 fab(5) 不会执行 fab 函数，而是返回一个 iterable 对象！
            在 for 循环执行时，每次循环都会执行 fab 函数内部的代码，执行到 yield b 时，fab 函数就返回一个迭代值，
            下次迭代时，代码从 yield b 的下一条语句继续执行，而函数的本地变量看起来和上次中断执行前是完全一样的，于是函数继续执行，直到再次遇到 yield。
    '''
    for n in Fab(6):
        print(n)
    
    #判断一个函数是否是generator函数
    print(isgeneratorfunction(Fab))
    
    for L in Triangles(5):
        print(L)
        
    for L in NewTrianbles(5):
        print(L)   
        
    
    
     
    pass

