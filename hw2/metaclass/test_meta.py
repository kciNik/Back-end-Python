import unittest
from meta_class import MyMeta


class TestMeta(unittest.TestCase):

    def test_values(self):
        class Test(metaclass=MyMeta):
            test_var_1 = 1
            test_var_2 = 2

        test = Test()
        self.assertNotIn('test_var_1', test.__dir__())
        self.assertNotIn('test_var_2', test.__dir__())
        self.assertIn('custom_test_var_1', test.__dir__())
        self.assertIn('custom_test_var_2', test.__dir__())
        self.assertEqual(test.custom_test_var_1, 1)
        self.assertEqual(test.custom_test_var_2, 2)
        with self.assertRaises(AttributeError):
            self.assertEqual(test.test_var_1, 1)
        with self.assertRaises(AttributeError):
            self.assertEqual(test.test_var_2, 2)

    def test_methods(self):
        class Test(metaclass=MyMeta):

            test_var = 1

            def check(self):
                return self.custom_test_var

        test = Test()
        self.assertNotIn('test_var', test.__dir__())
        self.assertNotIn('check', test.__dir__())
        self.assertIn('custom_test_var', test.__dir__())
        self.assertIn('custom_check', test.__dir__())
        self.assertEqual(test.custom_test_var, 1)
        self.assertEqual(test.custom_check(), 1)
        with self.assertRaises(AttributeError):
            self.assertEqual(test.test_var, 1)
        with self.assertRaises(AttributeError):
            self.assertEqual(test.check(), 1)

    def test_init(self):
        class Test(metaclass=MyMeta):

            test_var = 1

            def __init__(self, arg=2):
                self.test_var_2 = arg

            def check(self):
                return self.custom_test_var + self.custom_test_var_2

        test = Test()
        self.assertNotIn('test_var', test.__dir__())
        self.assertNotIn('test_var_2', test.__dir__())
        self.assertNotIn('check', test.__dir__())
        self.assertIn('custom_test_var', test.__dir__())
        self.assertIn('custom_test_var_2', test.__dir__())
        self.assertIn('custom_check', test.__dir__())
        self.assertEqual(test.custom_test_var, 1)
        self.assertEqual(test.custom_test_var_2, 2)
        self.assertEqual(test.custom_check(), 3)
        with self.assertRaises(AttributeError):
            self.assertEqual(test.test_var, 1)
        with self.assertRaises(AttributeError):
            self.assertEqual(test.test_var_2, 2)
        with self.assertRaises(AttributeError):
            self.assertEqual(test.check(), 3)


if __name__ == '__main__':
    unittest.main()
