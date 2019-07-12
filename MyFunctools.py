# -*- coding: utf-8 -*-

'''
Created on 2019年7月13号
偏函数
@author: XPF
'''

def int2(x, base1=2):
    return int(x, base1)

import functools

if __name__ == '__main__':
    
    #以十进制转换为int
    i= int('12345')
    print(i)
    
    #以8进制转换为int
    i = int('12345', base=8)
    print(i)
    
    #以2进制转换为int
    i = int2('10010', base1=2)
    print(i)
    
    int3 = functools.partial(int, base=2)
    i = int3('10010')
    print(i)
    
    max2 = functools.partial(max, 10)
    i = max2(5,6,7)
    print(i)
    pass