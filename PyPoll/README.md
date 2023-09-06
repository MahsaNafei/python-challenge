# Election Data Analysis Script

In this Python script (`main.py`), you will find an analysis of election data from a CSV file named `election_data.csv`. 

# Source of the Code

The source code for the Election Data Analysis script in this repository was developed for an assignment, Python Challenge. 

# Script Overview

This script accomplishes the following tasks:

1. **Data Retrieval**: It retrieves election data from the `election_data.csv` file located in the `Resources` directory.

2. **Data Analysis**:
    -Counting Total Votes Cast:
    To determine the total number of votes cast in the election, the script initializes a variable total_votes to zero.
    It then iterates through each row in the CSV file, incrementing the total_votes count for each row. This count represents the total participation in the election.
    The result is stored in the total_votes variable, which is later used to calculate the percentages of votes received by each candidate.

    -Calculating Candidate Votes and Percentages:

    The script maintains two data structures:
    1-candidate_name: A list to store the names of unique candidates.
    2-candidate_info: A dictionary where each candidate's name serves as the key, and the associated value is another dictionary containing the number of votes and their percentage.

    While iterating through the CSV file, it checks whether the candidate's name is already present in the candidate_info dictionary. If so, it increments the vote count for that candidate; otherwise, it adds the candidate's name to the candidate_name list and initializes their vote count to 1.
    After processing all the rows, the script calculates the percentage of votes each candidate received. It does this by dividing each candidate's vote count by the total_votes and then multiplying by 100 to get the percentage. The result is rounded to three decimal places for clarity.
    The calculated percentages are stored in the candidate_info dictionary, associated with each candidate's name.

3. **Results Display**: The script prints the election analysis results to the console, including the total number of votes, the percentage of votes for each candidate, and the winner of the election.

4. **Results Export**: It exports the election analysis results to a text file named `output.txt` located in the `analysis` directory.

# Instructions

To use this script:

1. Run the script using Python.
2. The analysis results will be displayed in the console and saved to `analysis/output.txt`.
