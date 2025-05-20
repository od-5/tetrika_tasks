import unittest

from solution import sum_two


class TestStrictDecorator(unittest.TestCase):

    def test_success(self):
        self.assertEqual(sum_two(1, 2), 3)

    def test_exception(self):
        with self.assertRaises(TypeError):
            sum_two(1.0, 2.0)


if __name__ == '__main__':
    unittest.main()
