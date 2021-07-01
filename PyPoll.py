# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate received
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# Add our dependencies.
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file
with open(file_to_load) as election_data:

    # To do: read and analyze the data.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read and print the header row in the CSV file.
    headers = next(file_reader)
    print(headers)
    
# Close the file.
election_data.close()

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    #Write title and add formatting
    txt_file.write("Counties in the Election")
    txt_file.write("\n-------------------------")

    # Write three counties to the file.
    txt_file.write("\nArapahoe\nDenver\nJefferson")
   

#Close the file.
txt_file.close()






