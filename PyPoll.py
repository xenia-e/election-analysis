#Data we need to retrieve
# 1. Total number of votes cast
# 2. A complete list of candidates who received votes
# 3. Total number of votes each candidate received
# 4. Percentage of votes each candidate won
# 5. The winner of the election based on popular vote

import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")


# 1. Initialize a total vote counter.
total_votes = 0

# Open the election results and read the file.
candidate_options = []
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
      # Print each row in the CSV file.
    for row in file_reader:
      # 2. Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row
        candidate_name = row[2]

        # Pick uniq names from the df
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        
        # 2. Begin tracking that candidate's vote count.
        candidate_votes[candidate_name] +=1

    for candidate_name in candidate_votes:
      votes = candidate_votes[candidate_name]
      votes_persentage = float(votes) / float(total_votes) * 100
      print(f"{candidate_name}: recieved {votes_persentage:.2f}% of votes")

     # Print the candidate list.
    print(candidate_votes)
   
  
