# Election analysis project


## Overview of Election Audit

Project goal is audit of recent local elections.

### Projects tasks
In this project, our final Python script will need to be able to deliver the following information: 
- Total number of votes cast
- A complete list of candidates who received votes
- Total number of votes each candidate received
- Percentage of votes each candidate won
- The winner of the election based on popular vote
- The voter turnout for each county
- The percentage of votes from each county out of the total count
- The county with the highest turnout

## Resources
- Data source: election_results.csv
- Python 3.7.10, Visual Studio Code 1.57.1 

# Election Audit Results


![Figure 1 - results of the election](https://github.com/xenia-e/election-analysis/blob/master/analysis/election_analysis.png)

>Figure 1 - Election analysis overview

The analysis of the election shows

- There were **total of 369,711 votes** in the election
- The counties were: 
		- Jefferson: 10.5% of votes (38,855)
		- Denver: 82.8% of votes (306,055)
		- Arapahoe: 6.7% of votes (24,801)
- **Denver** is the county with the highest turnout (82.8% of votes)
- The candidates were:
		- Charles Casper Stockham: 23.0% (85,213)
		- Diana DeGette: 73.8% (272,892)
		- Raymon Anthony Doane: 3.1% (11,606)
- The **winner of the election was Diana DeGette** with 73.8% of the votes (272,892 number of votes)

All data presented in [aelection_analysis.txt](https://github.com/xenia-e/election-analysis/blob/master/analysis/election_analysis.txt) file for further use.

## Election Audit Summary

Our script can be used to audit any elections simce it requires only a CSV file with relevant data to conduct it. In order to make the analysis more thorough, we could add the next points of analysis:

  1. Comparing the number of votes in counties with the number of the population eligible to vote to reveal the relative turnout at the elections.
  2. Analysis of votes for each candidate in each county would help us see local tendencies.   


