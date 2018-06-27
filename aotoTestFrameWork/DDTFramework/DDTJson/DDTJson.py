
import unittest
from ddt import ddt, file_data
from ddt_demo.mycode import has_three_elements, is_a_greeting


@ddt
class FooTestCase(unittest.TestCase):

    @file_data('test_data_dict.json')
    def test_file_data_json_dict(self, value):
        self.assertTrue(has_three_elements(value))

    @file_data('test_data_list.json')
    def test_file_data_json_list(self, value):
        self.assertTrue(is_a_greeting(value))


if __name__ == '__main__':
    unittest.main(verbosity=2)