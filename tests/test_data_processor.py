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
        cls.row = 3
        cls.row2 = 4
        cls.col = 4
        cls.df = pd.read_csv('../iris.data', sep=',', header=None)
        cls.mat = np.arange(0,12).reshape((3,4))
        cls.test = data_processor.get_random_matrix(cls.row, cls.col)
        cls.test2 = data_processor.get_random_matrix(cls.row2, cls.col)

    @classmethod
    def tearDownClass(cls):
        cls.row = None
        cls.col = None

    def test_get_random_matrix(self):
        self.assertEqual(data_processor.get_random_matrix(self.row, self.col), self.test)
        self.assertNotEqual(data_processor.get_random_matrix(self.row, self.col), self.test2)

    def test_get_file_dimensions(self):
        self.assertEqual(data_processor.get_file_dimensions(self.df), [150,5])
        self.assertNotEqual(data_processor.get_file_dimensions(self.df), [5,150])

    def test_write_matrix_to_file(self):
        self.assertEqual(data_processor.write_matrix_to_file(self.row, self.col, 'test.csv'), pathlib.Path('test.csv'))
        self.assertNotEqual(data_processor.write_matrix_to_file(self.row, self.col, 'test.csv'), pathlib.Path('t.csv'))


if __name__ == '__main__':
    unittest.main()