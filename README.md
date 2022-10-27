# libraries

THIS REPOSITORY CONTAINS TWO MAIN FILES. ONE A UTILITIES BASED FILE CONTAINING FUNCTIONS TO GET A RANDOM MATRIX N x M, ONE TO GET CSV FILE DIMENSIONS, AND THE LAST TO WRITE A RANDOM N x M MATRIX TO A FILE. THIS UTILITIES BASED FILE IS CALLED data_processor.py. THE SECOND BEING A SCRIPT THAT PERFORMS VARIOUS GRAPHING OPERATIONS ON THE iris.data DATASET. THIS SCRIPT WILL PROVIDE A VARIATION OF BOXPLOTS, SCATTER PLOTS, HISTROGRAM PLOTS, AND SUBPLOTS DEMONSTRATING THE POWER OF NUMPY, MATPLOTLIB, AND PANDAS LIBRARIES.

OVERARCHING GOALS:

The main goal of this repository is to demonstrate the power of libraries within the python ecosystem. We can see how easily we manipulate and plot data with these libraries compared to without. In addition this repo performs unit and functional testing, as well as CI through github actions. This ensures our programs and functions are doing what we expect them to do.

**The main script is:**
	
	plotter.py

This script plots a boxplot, scatterplot, and subplot containing a histogram and scatter plot of the iris.data dataset. This helps us visualize what is happening between various species of iris flowers and how easily it can be done with the help of useful libraries. Additionally:

	data_processor.py

Is a utilities based file that provides functions for random matrix generation, determining file dimensions, and writing matrices to csv files. These can be useful in many different circumstances, and I encourage you to try these out for your own project.

Testing:

	This repo is set up with CI and testing using Github Actions. Everything that makes its way on the the repository is subject to unit, function, and style testing via the testing.yml file.

	Use this file as a guide to set up Github actions for your needs.

	Additionally this repo also contains unit and functional test files. These are as follows:

	-- test_data_processor.py
	-- test_plotter.sh

	test_data_processor.py performs unit testing on the three functions in data_processor.py. These being get_random_matrix, get_file_dimensions, and write_matrix_to_file. This script when run provides unit testing on each of the functions to ensure they are performing properly.

	test_plotter.sh performs a function test of the plotter.py script to ensure it is also performing properly on a higher level.

To download the repo:

	git clone "https://github.com/cu-swe4s-fall-2022/assignment-7-using-libraries-collin-love"
