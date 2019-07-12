# -*- coding: utf-8 -*-
'''
Created on 2019��7��8��

@author: XPF
'''

def is_odd(n):
    return n % 2 == 1

if __name__ == '__main__':
    L = list(filter(is_odd, range(1, 20)))
    print(L)
    
    print(list(filter(lambda x : x % 2 == 1, range(1, 20))))
    
    pass