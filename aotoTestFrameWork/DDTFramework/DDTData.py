#coding=utf-8
'''
1.测试数据为多个字典的list类型
2.测试类前加修饰@ddt.ddt
3.case前加修饰@ddt.data()
4.运行后用例会自动加载成三个单独的用例
'''

#1.ddt直接放入数值
#需要导入ddt包，然后再TestCase类上采用@ddt进行装饰，测试方法上装饰@data()。
#data可以是数值，也可以是字符串。
import unittest
import ddt

from ddt import ddt,data


def add(x,y):
    return x+y
@ddt
class FooTestCase(unittest.TestCase):
    @data(3, 4, 12, 23)
    def test_larger_than_two(self,value):
        self.assertEqual(add(2,1),value)
    @data(1, -3, 2, 0)
    def test_not_larger_than_two(self,value):
        self.assertEqual(add(1,1),value)
    @data(u'ascii', u'non-ascii-\N{SNOWMAN}')
    def test_unicode(self, value):
        self.assertIn(value, (u'ascii', u'non-ascii-\N{SNOWMAN}'))

if __name__=='__main__':
    unittest.main()

