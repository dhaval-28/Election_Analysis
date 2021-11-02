# Add our dependencies.
import os
import csv

# Assign a variable for the file to load and  file to save  path.
file_to_load_path =os.path.join('Resources','election_results.csv')

# Assign a variable for the file to save  path.
file_to_save_path = os.path.join('Analysis','election_analysis.txt')

# set total_votes counter to zero
total_votes = 0 

# candidate options - create empty list
candidate_options_list = []

# candidate votes - create empty dictionary
candidate_votes_dict = {}

# Winning Candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0


with open(file_to_load_path,'r') as election_data :
#   print(election_data)

# Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read the file and print all rows
    #for row in file_reader:
        #print(row) # to print file
        #print(row[0]) # to print first column only        
    # Read and print the header row.
    headers = next(file_reader) # skip the first row from the count and analysis
    #print(headers)

    for file_row_reading_loop in file_reader:   # row is a loop name, can put any name

        #1 A total number of votes cast, counting total rows excluding header
        total_votes += 1

        #2 A complete list of candidates who received votes
        candidate_name = file_row_reading_loop[2]
        if candidate_name not in candidate_options_list:
            candidate_options_list.append(candidate_name)

        #3 Total votes per each candidate
            candidate_votes_dict[candidate_name] = 0       #####???????? how does data dict know my keys are candidate name
        candidate_votes_dict[candidate_name] += 1  

# Save the results to our text file.
with open(file_to_save_path,"w") as txt_file:
    election_results =(
        f"\nElections Results \n"
        f"----------------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"----------------------------------\n")
    print(election_results, end = "")
    txt_file.write(election_results)

        # 4 Determine the percentage of votes for each candidate by looping through the counts.
        # 4(1). Iterate through the candidate list.
    for candidate_name in candidate_votes_dict:     #####?????? why loop name is dictionary
        # 4(2). Retrieve vote count of a candidate.
        votes = candidate_votes_dict[candidate_name]  #####???????? specifiying dict name and key , would that reference the values, votes per candidate in this case? 
        # 4(3). Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100  ## float(candidate_votes_dict[candidate_name]) / float(total_votes) * 100
        # 4(4). Print the candidate name and percentage of votes.
        #print(f"{candidate_name}: received {vote_percentage:.2f}% ({votes:,})\n")  #####???????? why indenent matter
        candidate_results = (f"{candidate_name}: received {vote_percentage:.2f}% ({votes:,})\n")
        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)   

    #5 The winner of the election based on the popular votes.  Determine winning vote count and candidate
        #5(1) Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
            winning_candidate_summary =  (
                f"-----------------------\n"
                f"Winner: {winning_candidate}\n"
                f"winning Vote Count : {winning_count}\n"
                f"Winning Percentage: {winning_percentage:.2f}%\n"
                f"-----------------------\n")
    # Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)

# print(f'-----------------------\n# 1 total number of votes casted = {total_votes}\n-----------------------')
# print(f'# 2 candidate_options_list list is  {candidate_options_list}\n-----------------------')
# print (f'# 3candidate_votes_dict dictionary is {candidate_votes_dict}\n-----------------------')
# print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
# print (winning_candidate_summary)



# Write results to text file
#with open(file_to_save_path,'w') as txt_result_file :
    #txt_result_file.write('Hello World')



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
