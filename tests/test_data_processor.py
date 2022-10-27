import unittest
import os
import pathlib
import random
import sys
import pandas as pd
import numpy as np
sys.path.append('../')
import data_processor  # nopep8


class TestUtils(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # np.random.seed(7)
        cls.row = 3
        cls.row2 = 4
        cls.col = 4
        cls.df = '../iris.data'
        cls.mat = np.arange(0, 12).reshape((3, 4))
        cls.test = data_processor.get_random_matrix(cls.row, cls.col)
        cls.test2 = data_processor.get_random_matrix(cls.row2, cls.col)
        cls.shorten = data_processor.write_matrix_to_file(cls.row,
                                                          cls.col,
                                                          'test.csv')

    @classmethod
    def tearDownClass(cls):
        cls.row = None
        cls.col = None

    def test_get_random_matrix(self):
        self.assertTrue(np.array_equal(self.test, self.test, equal_nan=True))
        self.assertFalse(np.array_equal(self.test, self.test2, equal_nan=True))

    def test_get_file_dimensions(self):
        self.assertEqual(data_processor.get_file_dimensions(self.df),
                         (150, 5))
        self.assertNotEqual(data_processor.get_file_dimensions(self.df),
                            (5, 150))

    def test_write_matrix_to_file(self):
        self.assertTrue(pathlib.Path('../test.csv'))


if __name__ == '__main__':
    unittest.main()
