# PyBank Financial Analysis Script

In this Python script (`main.py`), you will find a detailed analysis of financial data from a CSV file named `budget_data.csv`. 

# Source of the Code

The source code for the PyBank financial analysis script in this repository in this repository was developed for an assignment, Python Challenge. 

# Script Overview

This script accomplishes the following tasks:

1. **Data Retrieval**: It retrieves financial data from the `budget_data.csv` file located in the `Resources` directory.

2. **Data Analysis**:

    -Inside a loop, it calculates:
    totalmonths: Incremented for each row, representing the total number of months in the dataset.
    totalvalue: Accumulated by adding the profit/loss value from each row.
    changes: Appends the calculated change in profit/loss for each month.
    date: Appends the corresponding date for each month.
    It also calculates the average change by dividing the change in the last month by the total number of months minus one. The result is rounded to two decimal places.

    -Data Cleaning:
    The script creates clean_csv, a list of tuples containing date and change pairs. This will be used to identify the month with the greatest increase and decrease in profits.

    -Finding Greatest Increase and Decrease:
    It identifies the month with the greatest increase and decrease in profits by filtering the clean_csv list using list comprehensions.
    greatest_increase stores the month with the highest profit increase.
    greatest_decrease stores the month with the highest profit decrease.

3. **Results Display**: The script prints the financial analysis results to the console, including total months, total profit/loss, average change, greatest increase in profits, and greatest decrease in profits.

4. **Results Export**: It exports the financial analysis results to a text file named `output.txt` located in the `analysis` directory.

# Instructions

To use this script:

1. Run the script using Python.
2. The analysis results will be displayed in the console and saved to `analysis/output.txt`.
