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
file_to_save = os.path.join("Resources", "election_results.txt")


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
    
  # Save the results to txt file.
    with open(file_to_save, "w") as txt_file:
      # Final vote count
      election_results = (
        f"\nELECTION RESULTS\n"
        f"---------------------------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"---------------------------------------------\n\n")
      print(election_results, end="")
      # Save the final vote count to the text file.
      txt_file.write(election_results)

      for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        votes_percentage = float(votes) / float(total_votes) * 100
        # Print the candidates summary list.
        candidate_results = (f"{candidate_name}: {votes_percentage:.1f}% of votes ({votes:,})\n\n")
        # Print each candidate results to the terminal.
        print(candidate_results)
        #  Save the candidate results to txt file.
        txt_file.write(candidate_results)

        # determing the winner
        if (votes > winning_count) and (votes_percentage > winning_percentage):
          winning_count = votes
          winning_percentage = votes_percentage
          winning_candidate = candidate_name

      # wining candidate summary  
      winning_candidate_summary = (
          f"---------------------------------------------\n"
          f"Winner: {winning_candidate}\n"
          f"Winning Vote Count: {winning_count:,}\n"
          f"Winning Percentage: {winning_percentage:.1f}%\n"
          f"---------------------------------------------\n")
      print(winning_candidate_summary)
      # Save the winning winning summary to the txt file.
      txt_file.write(winning_candidate_summary)



   
  
