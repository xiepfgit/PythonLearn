# -*- coding: utf-8 -*-

'''
Created on 2019��7��16��

了解访问限制、继承多肽、对象信息、实例属性和类属性
@author: XPF
'''

import types
    
    
from collections import __main__
from builtins import int

class MyClassBase(object):
    '''
    classdocs
    '''
    
class MyClass(MyClassBase):
    '''
    classdocs
    '''

    #私有成员
    name1 = 'classname'
    

    def __init__(self, name, count, proPra, pubPra):
        '''
        Constructor
        '''
        self.__name = name
        self.__count = count
        self._proPra = proPra
        self.pubPra = pubPra
        
    def get_name(self):
        return self.__name
    
    def get_count(self):
        return self.__count
      
    def get_proPra(self):
        return self._proPra
    
    

#动态语言的特性

class Person(object):
    def __init__(self, name):
        self.__name = name
    
    def get_name(self):
        return self.__name

    
def TestFunc(test):
    return test.get_name()


#不能只是写一个类名，至少添加一些注释说明，如果没有注释，则下面if语句会报错
class test(object):
    pass
            
        
if __name__ == '__main__':
    myclass = MyClass('myclass', 50, 'proPra', 'pubPra')
    print(myclass.get_name())
    print(myclass.get_count())
    print(myclass.get_proPra())
    print(myclass.pubPra)
    
    #私有成员可以通过以下方式获取，但是强烈建议你不要这么干，因为不同版本的Python解释器可能会把__name改成不同的变量名。
    print(myclass._MyClass__name)
    
    #动态语言特性：鸭子类型，函数对参数test只有一个要求，实现get_name方法
    #而对myclass 和 person都实现了这些方法，所以他们的实例对象都可以用作TestFunc的参数
    #动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的。
    person = Person('xpf')
    print(TestFunc(person))
    print(TestFunc(myclass))
    
    print(type(123) == type(456))
    print(type(789) == int)
    
    #函数类型
    print(type(TestFunc) == types.FunctionType)
    print(type(abs) == types.BuiltinFunctionType)
    print(type(lambda x:x) == types.LambdaType)
    print(type(x for x in range(10)) == types.GeneratorType)
    
    print('*******************************')
    print(isinstance(myclass, MyClass))
    print(isinstance(myclass, MyClassBase))
    print(isinstance(person, Person))
    
    #如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，
    #比如，获得一个str对象的所有属性和方法：
    print(dir(myclass))
    
    
    print(myclass.name1)
    print(MyClass.name1)
    myclass.name1 = 'myclassname'
    #
    print(myclass.name1)
    print(MyClass.name1)
    # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
    ## 但是类属性并未消失，MyClass.name1仍然可以访问
    
    #从下面的地址也能看出二者不是同一变量
    print(id(myclass.name1))
    print(id(MyClass.name1))
    
    print(type(id))
    print(type(int))
    #如果删除实例的name属性
    #由于实例的name属性没有找到，类的name属性就显示出来了
    del myclass.name1
    print(myclass.name1)