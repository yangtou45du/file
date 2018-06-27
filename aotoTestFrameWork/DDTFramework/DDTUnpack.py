#coding=utf-8
'''装饰测试方法。参数是文件名。文件可以是json 或者 yaml类型。

注意，如果文件以”.yml”或者”.yaml”结尾，ddt会作为yaml类型处理，其他所有文件都会作为json文件处理。

如果文件中是列表，每个列表的值会作为测试用例参数，同时作为测试用例方法名后缀显示。

如果文件中是字典，字典的key会作为测试用例方法的后缀显示，字典的值会作为测试用例参数'''
import unittest
from ddt import ddt,data,unpack
#2. data放入复杂的数据结构
@ddt
class FooTestCase(unittest.TestCase):
    @data((3,2),(4,3),(5,3))
    @unpack
    def test_tuples_extracted_into_arguments(self,first_value,second_value):
        self.assertTrue(first_value>second_value)
    @data([3,2],[4,3],[5,3])
    @unpack
    def test_list_extracted_into_arguments(self,first_value,second_value):
        self.assertTrue(first_value > second_value)

    @unpack
    @data({'first': 1, 'second': 3, 'third': 2},
          {'first': 4, 'second': 6, 'third': 5})
    def test_dicts_extracted_into_kwargs(self, first, second, third):
        self.assertTrue(first < third < second)
if __name__=='__main__':
    unittest.main()