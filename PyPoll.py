#1 The data we need to retrieve # Resources/election_results.csv
import os
import csv

# Assign a variable for the file to load and  file to save  path.
file_to_load_path =os.path.join('Resources','election_results.csv')
file_to_save_path = os.path.join('Analysis','election_analysis.txt')

with open(file_to_load_path,'r') as election_data :
 #   print(election_data)

# Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    for row in file_reader:
        print(row)
        # to print first column only print(row[0])
    # Read and print the header row.
    headers = next(file_reader)
    print(headers)

# Write results to text file
with open(file_to_save_path,'w') as txt_result_file :
    txt_result_file.write('Hello World')

#2 A total number of votes cast
#3 A complete list of candidates who received votes
#4 The percentage of votes each candiate got
#5 The toal number of votes each cndidate got
#6 The winner of the election based on the popular votes.


# # Import the datetime class from the datetime module.
# import datetime
# # Use the now() attribute on the datetime class to get the present time.
# now = datetime.datetime.now()
# # Print the present time.
# print("The time right now is ", now)


# ## import date
# from datetime import timestamp
# # Use the now() attribute on the datetime class to get the present time.
# today = timestamp.today()
# # Print the present time.
# print("Today's date is ", today)


# import csv
# dir (csv)
