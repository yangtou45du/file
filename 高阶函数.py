#!/usr/bin/python
# -*- coding: cp936 -*-
# -*- coding: encoding -*-

#map()������������������һ���Ǻ�����һ�������У�map������ĺ����������õ����е�ÿ��Ԫ�أ����ѽ����Ϊ�µ�list����
a=map(str,[1,2,3])
print type(a)
def fun(x):
    return x*x
b=map(fun,[1,2,3,4])
print b
#reduce��һ������������һ������[x1, x2, x3...]�ϣ�������������������������reduce�ѽ�����������е���һ��Ԫ�����ۻ�����
#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
def fun1(x,y):
    return x+y
c=reduce(fun1,[1,2,3,4])#�൱��1+2+3+4
print c
