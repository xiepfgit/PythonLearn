# -*- coding: utf-8 -*-

'''
Created on 2019��6��4��

@author: XPF
'''

if __name__ == '__main__':
    print('*******************************\n')
    
    #List：用[]表示
    classmates = ['Michael', 'Bob', 'Tracy']
    print(classmates)
    
    print(len(classmates))
    
    print(classmates[0])
    
    print(classmates[-1])
    
    classmates.insert(1, 'Jack')
    print(classmates)
    
    classmates.pop(1)
    print(classmates)
    
    classmates[1] = 'Sarah'
    print(classmates)
    
    L = ['Apple', 123, True]
    print(L)

    s = ['python',  'java', ['asp', 'php'], 'scheme']
    print(s)
    print(len(s))
    
    #tuple 元组，用()表示
    classmates = ('Michael', 'Bob', 'Tracy')
    print(classmates)
    #空的tuple
    t = ()
    print(len(t))
    
    #定义为元组：只有1个元素的tuple定义时必须加一个逗号,，来消除歧义：
    #这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义
    t = (1,)
    #定义为数
    n = (1)
    
    #其中变的并不是元组t，元组内部t指向那个List没变，但是那个List中的元素变了所以导致输出结果变了
    t = ('a', 'b', ['A', 'B'])
    t[2][0] = 'X'
    t[2][1] = 'Y'
    print(t)
    
    #dict是用空间来换取时间的一种方法。
    #dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象。
    dic1 = {'Michael':95, 'Bob':75, 'Tracy':85}   
    print(dic1['Michael'])
    
    #判断字典中是否存在key值
    print('Toms' in dic1)
    print(dic1.get('Toms'))
    print(dic1.get('Toms'), -1)
    
    #要保证key值是唯一对象，所以需要key必须要不可变，一下两行代码是错误的。
    #key = [1,2,3]
    #dic1[key] = 'a list'
    
    
    #set是一组Key的无序的集合，但是不存储value。由于key不能重复，所以在set中，没有重复的key。
    #要创建一个set集合，需要提供一个list作为输入集合。
    s = set([1,2,3])
    print(s)
    #自动过滤重复的集合
    s = set([1,1,3,3,2,2])
    print(s)
    #集合内部元素数
    print(s.__len__())
    
    s.add(4)
    s.add('2')
    print(s)
    
    s.remove(4)
    
    print( s.__contains__('1'))
    #s.remove('1')
    print(s)
    #求交集
    s1 = set([1,2,3])
    s2 = set([2,3,4])
    print(s1 & s2)
    
    #a是不可变对象，replace函数只是新建了一块内存b,把这个替换后的结果放入b中。
    a = 'abc'
    b = a.replace('a', 'A')
    print(a)
    print(b)
    
    
    
    
    pass
