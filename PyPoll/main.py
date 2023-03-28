# This is the script for the directory PyPoll of the python challenge. Importing modules first
import os
import csv

# Determine the paths to and from the csv file

election_path = os.path.join("Resources", "election_data.csv")
output_path = os.path.join("Analysis", "ElectionData_Analysis.txt")

# Lists to store data
voterId = []
counties = []
candidates = []
# Commented next list out because it is not necessary but I used it to find the unique candidates.
# unique_candidates = [] 
final_counts = {}


# Open and read csv file
with open(election_path) as electionFile:
    efReader = csv.reader(electionFile, delimiter=",")

    electionFile_header = next(efReader)

    # A for Loop to read each row of data after the header and append data to the empty lists
    for row in efReader:

        # Adding the voters to a list
        voterId.append(row[0])

        # Adding the counties to a list. This line is not necessary, but I will keep all the information here.
        # counties.append(row[1])

        # Adding the candidates to a list
        candidates.append(row[2])

    # Finding the unique candidates. 
    # I only used this line to obtain the candidates. I will comment it out for now
    # unique_candidates = list(set(candidates))
    # print(unique_candidates)

    # Get Total numbers of votes cast
    Total_votes = (len(voterId))

    # Count the number of votes each candidate got

    count_CCS = candidates.count("Charles Casper Stockham")
    percentage_CCS = round((count_CCS/Total_votes*100), 3)

    count_DDG = candidates.count("Diana DeGette")
    percentage_DDG = round((count_DDG/Total_votes*100), 3)
    
    count_RAD = candidates.count("Raymon Anthony Doane")
    percentage_RAD = round((count_RAD/Total_votes*100), 3)
    
    # Dictionary to iterate through the candidates and votes 
    final_counts = {"Charles Casper Stockham":count_CCS,
                    "Diana DeGette": count_DDG, 
                    "Raymon Anthony Doane": count_RAD}
    
    # Finding the winner 
    winnerName = max(final_counts, key=final_counts.get)
    
    
    # String concatenation for printing results
    result = ""
    result += "Election Results\n"
    result += "------------------------\n"
    result += f"Total Votes: {Total_votes} \n"
    result += "------------------------------ \n"
    result += f"Charles Casper Stockham: {percentage_CCS}% ({count_CCS}) \n"
    result += f"Diana DeGette: {percentage_DDG}% ({count_DDG}) \n"
    result += f"Raymon Anthony Doane: {percentage_RAD}% ({count_RAD}) \n"
    result += "------------------------------ \n"
    result += f"Winner : {winnerName} \n"
    result += "-------------------------------"
    print(result)
    
    
    # Writing text file
    with open(output_path, "w") as file:
        file.write(result)
   
# END OF CODE
###########################################################################################

