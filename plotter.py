# Your code to create majestic plots goes in here!
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys


def main():
    # iris boxplot
    iris = pd.read_csv('iris.data', sep=',', header=None)
    iris.columns = ['sepal_width',
                    'sepal_length',
                    'petal_width',
                    'petal_length',
                    'species']

    measurement_names = ['sepal_width', 'sepal_length',
                         'petal_width', 'petal_length']

    plt.boxplot(iris[measurement_names], labels=measurement_names)
    plt.ylabel('cm')
    plt.show()

    # iris petal width v length scatter
    for species_name in set(iris['species']):
        iris_subset = iris[iris['species'] == species_name]
        plt.scatter(iris_subset['petal_width'],
                    iris_subset['petal_length'],
                    label=species_name, s=5)

    plt.legend()
    plt.xlabel('petal_width')
    plt.ylabel('petal_length')
    plt.title('Iris Petal Width vs Length')
    plt.show()

    # multipanel figure
    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.set_size_inches(12, 5)

    for species_name in set(iris['species']):
        iris_subset = iris[iris['species'] == species_name]
        ax2.scatter(iris_subset['petal_width'],
                    iris_subset['petal_length'],
                    label=species_name, s=5)

    ax2.legend()
    ax2.set_xlabel('petal_width')
    ax2.set_ylabel('petal_length')

    ax1.boxplot(iris[measurement_names], labels=measurement_names)
    ax1.set_ylabel('cm')

    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)

    plt.show()


if __name__ == '__main__':
    main()
