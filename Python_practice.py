
counties = ["Arapahoe","Denver","Jefferson"]
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}




for county, voters in counties_dict.items():
  print(county, ' county has registered ', voters, 'voters')

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]


for county_dict in voting_data:
    for value in county_dict.values():
        print(value)


# to print only numbers
for county_dict in voting_data:
     print(county_dict['registered_voters'])

# to print only names
for county_dict in voting_data:
    print(county_dict['county'])

#using f-string in print()

for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")

#multilines f-string

candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")

print(message_to_candidate)



  # Print the file object.
  print(election_data)

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

  # Write three counties to the file.
  txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")