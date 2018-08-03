

import unittest

import list_lib


class TestLibMethods(unittest.TestCase):

    # index_of

    def test_index_of_empty(self):
        self.assertEqual(list_lib.index_of([], 42), list_lib.NOT_FOUND)

    def test_index_of_not_found(self):
        self.assertEqual(list_lib.index_of([1, 2, 3], 42), list_lib.NOT_FOUND)

    def test_index_of_first(self):
        self.assertEqual(list_lib.index_of([1, 2, 3], 1), 0)

    def test_index_of_middle(self):
        self.assertEqual(list_lib.index_of([1, 2, 3], 2), 1)

    def test_index_of_last(self):
        self.assertEqual(list_lib.index_of([1, 2, 3], 3), 2)

    def test_index_of_multiple(self):
        self.assertEqual(list_lib.index_of([1, 2, 2], 2), 1)

    def test_index_of_none(self):
        with self.assertRaises(TypeError):
            list_lib.index_of(None, 42)

    # contains

    def test_contains_empty(self):
        self.assertFalse(list_lib.contains([], 42))

    def test_contains_not_found(self):
        self.assertFalse(list_lib.contains([1, 2, 3], 42))

    def test_contains_found(self):
        list = [1, 2, 3]
        for item in list:
            self.assertTrue(list_lib.contains(list, item))

    def test_contains_none(self):
        with self.assertRaises(TypeError):
            list_lib.contains(None, 42)

    # sum_list

    def test_sum_list_empty(self):
        self.fail("Test not implemented")

    def test_sum_list_sum(self):
        self.assertEqual(list_lib.sum_list([1, 2, 3]), 6)

    def test_sum_list_none(self):
        self.fail("Test not implemented")

    # max_list

    def test_max_list_empty(self):
        with self.assertRaises(IndexError):
            list_lib.max_list([])

    def test_max_list_first(self):
        self.assertEqual(list_lib.max_list([3, 2, 1]), 3)

    def test_max_list_middle(self):
        self.fail("Test not implemented")

    def test_max_list_last(self):
        self.fail("Test not implemented")

    def test_max_list_multiple(self):
        self.fail("Test not implemented")

    def test_max_list_none(self):
        self.fail("Test not implemented")


if __name__ == '__main__':
    unittest.main()

