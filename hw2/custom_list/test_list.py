from list import CustomList
import unittest


class TestList(unittest.TestCase):

    def test_creation(self):
        test = CustomList()
        with self.assertRaises(IndexError):
            test[0] = 0
        test.append(0)
        self.assertEqual(0, test[0])
        self.assertEqual(1, len(test))
        test_1 = CustomList(1, 2, 3)
        self.assertEqual(1, test_1[0])
        self.assertEqual(3, len(test_1))

    def test_add_custom_list(self):
        first_str = CustomList(1, 2)
        sec_str = CustomList(3, 4)
        res = first_str + sec_str
        self.assertIsInstance(res, CustomList)
        self.assertEqual(res[0], 4)
        self.assertEqual(res[1], 6)

        first_str = CustomList(1, 2, 3)
        sec_str = CustomList(4, 5)
        res = first_str + sec_str
        self.assertIsInstance(res, CustomList)
        self.assertEqual(res[0], 5)
        self.assertEqual(res[1], 7)
        self.assertEqual(res[2], 3)

        first_str = CustomList(1, 2)
        sec_str = CustomList(3, 4, 5)
        res = first_str + sec_str
        self.assertIsInstance(res, CustomList)
        self.assertEqual(res[0], 4)
        self.assertEqual(res[1], 6)
        self.assertEqual(res[2], 5)

    def test_add_usual_list(self):
        first_str = CustomList(1, 2)
        sec_str = [3, 4]
        res = first_str + sec_str
        self.assertIsInstance(res, CustomList)
        self.assertEqual(res[0], 4)
        self.assertEqual(res[1], 6)
        res = first_str + sec_str
        self.assertIsInstance(res, CustomList)
        self.assertEqual(res[0], 4)
        self.assertEqual(res[1], 6)

        first_str = CustomList(1, 2, 3)
        sec_str = [4, 5]
        res = first_str + sec_str
        self.assertIsInstance(res, CustomList)
        self.assertEqual(res[0], 5)
        self.assertEqual(res[1], 7)
        self.assertEqual(res[2], 3)
        res = first_str + sec_str
        self.assertIsInstance(res, CustomList)
        self.assertEqual(res[0], 5)
        self.assertEqual(res[1], 7)
        self.assertEqual(res[2], 3)

        first_str = CustomList(1, 2)
        sec_str = [3, 4, 5]
        res = first_str + sec_str
        self.assertIsInstance(res, CustomList)
        self.assertEqual(res[0], 4)
        self.assertEqual(res[1], 6)
        self.assertEqual(res[2], 5)
        res = first_str + sec_str
        self.assertIsInstance(res, CustomList)
        self.assertEqual(res[0], 4)
        self.assertEqual(res[1], 6)
        self.assertEqual(res[2], 5)

    def test_add_assign(self):
        first_str = CustomList(1, 2)
        sec_str = CustomList(3, 4)
        first_str += sec_str
        self.assertEqual(first_str[0], 4)
        self.assertEqual(first_str[1], 6)

        first_str = CustomList(1, 2)
        sec_str = [3, 4]
        first_str += sec_str
        self.assertEqual(first_str[0], 4)
        self.assertEqual(first_str[1], 6)

        first_str = CustomList(1, 2, 3)
        sec_str = [4, 5]
        first_str += sec_str
        self.assertEqual(first_str[0], 5)
        self.assertEqual(first_str[1], 7)
        self.assertEqual(first_str[2], 3)

        first_str = CustomList(1, 2)
        sec_str = [3, 4, 5]
        first_str += sec_str
        self.assertEqual(first_str[0], 4)
        self.assertEqual(first_str[1], 6)
        self.assertEqual(first_str[2], 5)

    def test_sub_custom_list(self):
        first_str = CustomList(1, 2)
        sec_str = CustomList(3, 4)
        res = first_str - sec_str
        self.assertIsInstance(res, CustomList)
        self.assertEqual(res[0], -2)
        self.assertEqual(res[1], -2)
        res = sec_str - first_str
        self.assertIsInstance(res, CustomList)
        self.assertEqual(res[0], 2)
        self.assertEqual(res[1], 2)

        first_str = CustomList(1, 2, 3)
        sec_str = CustomList(4, 5)
        res = first_str - sec_str
        self.assertIsInstance(res, CustomList)
        self.assertEqual(res[0], -3)
        self.assertEqual(res[1], -3)
        self.assertEqual(res[2], 3)
        res = sec_str - first_str
        self.assertIsInstance(res, CustomList)
        self.assertEqual(res[0], 3)
        self.assertEqual(res[1], 3)
        self.assertEqual(res[2], -3)

        first_str = CustomList(1, 2)
        sec_str = CustomList(3, 4, 5)
        res = first_str - sec_str
        self.assertIsInstance(res, CustomList)
        self.assertEqual(res[0], -2)
        self.assertEqual(res[1], -2)
        self.assertEqual(res[2], -5)
        res = sec_str - first_str
        self.assertIsInstance(res, CustomList)
        self.assertEqual(res[0], 2)
        self.assertEqual(res[1], 2)
        self.assertEqual(res[2], 5)

    def test_sub_usual_list(self):
        first_str = CustomList(1, 2)
        sec_str = [3, 4]
        res = first_str - sec_str
        self.assertIsInstance(res, CustomList)
        self.assertEqual(res[0], -2)
        self.assertEqual(res[1], -2)
        res = sec_str - first_str
        self.assertIsInstance(res, CustomList)
        self.assertEqual(res[0], 2)
        self.assertEqual(res[1], 2)

        first_str = CustomList(1, 2, 3)
        sec_str = [4, 5]
        res = first_str - sec_str
        self.assertIsInstance(res, CustomList)
        self.assertEqual(res[0], -3)
        self.assertEqual(res[1], -3)
        self.assertEqual(res[2], 3)
        res = sec_str - first_str
        self.assertIsInstance(res, CustomList)
        self.assertEqual(res[0], 3)
        self.assertEqual(res[1], 3)
        self.assertEqual(res[2], -3)

        first_str = CustomList(1, 2)
        sec_str = [3, 4, 5]
        res = first_str - sec_str
        self.assertIsInstance(res, CustomList)
        self.assertEqual(res[0], -2)
        self.assertEqual(res[1], -2)
        self.assertEqual(res[2], -5)
        res = sec_str - first_str
        self.assertIsInstance(res, CustomList)
        self.assertEqual(res[0], 2)
        self.assertEqual(res[1], 2)
        self.assertEqual(res[2], 5)

    def test_sub_assign(self):
        first_str = CustomList(1, 2)
        sec_str = CustomList(3, 4)
        first_str -= sec_str
        self.assertEqual(first_str[0], -2)
        self.assertEqual(first_str[1], -2)

        first_str = CustomList(1, 2)
        sec_str = [3, 4]
        first_str -= sec_str
        self.assertEqual(first_str[0], -2)
        self.assertEqual(first_str[1], -2)

        first_str = CustomList(1, 2, 3)
        sec_str = [4, 5]
        first_str -= sec_str
        self.assertEqual(first_str[0], -3)
        self.assertEqual(first_str[1], -3)
        self.assertEqual(first_str[2], 3)

        first_str = CustomList(1, 2)
        sec_str = [3, 4, 5]
        first_str -= sec_str
        self.assertEqual(first_str[0], -2)
        self.assertEqual(first_str[1], -2)
        self.assertEqual(first_str[2], -5)

    def test_eq(self):
        first_str = CustomList(1, 2, 3)
        sec_str = CustomList(4, 2)
        self.assertTrue(first_str == sec_str)
        third_str = [0, 0, 1]
        self.assertFalse(first_str == third_str)

    def test_ne(self):
        first_str = CustomList(1, 2, 3)
        sec_str = CustomList(4, 2)
        self.assertFalse(first_str != sec_str)
        third_str = [0, 0, 1]
        self.assertTrue(first_str != third_str)

    def test_lt(self):
        first_str = CustomList(1, 2, 3)
        sec_str = CustomList(4, 2)
        self.assertFalse(first_str < sec_str)
        third_str = [5, 1, 1]
        self.assertTrue(first_str < third_str)

    def test_gt(self):
        first_str = CustomList(1, 2, 3)
        sec_str = CustomList(4, 2)
        self.assertFalse(first_str > sec_str)
        third_str = [5, 0, 0]
        self.assertTrue(first_str > third_str)

    def test_le(self):
        first_str = CustomList(1, 2, 3)
        sec_str = CustomList(4, 1)
        self.assertFalse(first_str <= sec_str)
        third_str = [5, 1]
        self.assertTrue(first_str <= third_str)
        third_str.append(1)
        self.assertTrue(first_str <= third_str)

    def test_ge(self):
        first_str = CustomList(1, 2, 3)
        sec_str = CustomList(4, 3)
        self.assertFalse(first_str >= sec_str)
        third_str = [5, 0]
        self.assertTrue(first_str >= third_str)
        third_str.append(1)
        self.assertTrue(first_str >= third_str)


if __name__ == '__main__':
    unittest.main()
