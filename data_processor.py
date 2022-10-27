# remember to import your libraries!
import numpy as np
import pandas as pd


def get_random_matrix(num_rows, num_columns):
    mat = np.random.rand(num_rows, num_columns)
    return mat


def get_file_dimensions(file_name):
    df = pd.read_csv(file_name, sep=',', header=None)
    dims = df.shape
    return dims


def write_matrix_to_file(num_rows, num_columns, file_name):
    mat = np.random.rand(num_rows, num_columns)
    np.savetxt(file_name, mat, delimiter=',')
    return None
