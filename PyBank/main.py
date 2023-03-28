# This is the script for the directory PyBank of the python challenge. Importing modules first
import os
import csv

# Determine the path to and from the csv file

budget_path = os.path.join("Resources", "budget_data.csv")
output_path = os.path.join('Analysis', 'FinancialAnalysis_Final.txt')

# Lists to store data
months = []
prof_loss = []
changeover_period = []
average_change = []
month_maxincrease = []
month_maxdecrease = []


# Open and read csv file
with open (budget_path) as budgetFile:
    bfReader = csv.reader(budgetFile, delimiter=",")

    budgetFile_header = next(bfReader)
    
    # Start by defining total as 0
    total = 0

    # A for Loop to read each row of data after the header and append data to the empty lists
    for row in bfReader:

        # Adding the months to the list
        months.append(row[0])    

        # Adding the profit/losses 
        prof_loss.append(int(row[1]))
    
        # Defining new total
        total += int(row[1])   

    # Count months
    countMonths = len(months)
    
    # Calculating change over period and appending to the list
    changeover_period = [((prof_loss[i + 1])-(prof_loss[i])) for i in range(countMonths-1)]

    # For average change we sum all changes over period and divide by the number of months minus 1 
    # (because we did substructions before and now we have one less value)
    average_change = round((sum(changeover_period)/(countMonths-1)), 2)
    
    # Find the Greatest increase 
    maxincrease = max(changeover_period)

    # Find month of greatest increase
    month_maxincrease = [months[j + 1] for j in range(len(changeover_period)) if changeover_period[j] == max(changeover_period)]
    
    # Find the Greatest Decrease
    minincrease = min(changeover_period)
    
    # Find month of greatest decrease
    month_maxdecrease = [months[j + 1] for j in range(len(changeover_period)) if changeover_period[j] == min(changeover_period)]
    

    # String concatenation for printing results
    result = ""
    result += "Financial Analysis\n"
    result += "------------------------\n"
    result += f"Total Months: {countMonths} \n"
    result += f"Total: ${total} \n"
    result += f"Average Change: ${float(average_change)} \n"
    result += f"Greatest Increase in Profits: {month_maxincrease} (${maxincrease}) \n"
    result += f"Greatest Decrease in Profits: {month_maxdecrease} (${minincrease})"
    print(result)

    
    # Writing text file
    with open(output_path, "w") as file:
        file.write(result)
   
# END OF CODE
###########################################################################################
