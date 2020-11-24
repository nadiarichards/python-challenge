import os
import csv

# Path to collect data from the Resources folder
budget_csv = os.path.join('..', 'Resources', 'budget_data.csv')

#The total number of months included in the dataset
#Name first and 2nd column
# Define the function 
def print_total (budget_data):
    # For readability, it can help to assign your values to variables with descriptive names
    date = str(budget_data[0])
    profit_losses = int(budget_data[1])

with open(budget_csv, "r") as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter = ",")
    data = list(csvreader)
    #header = next(csvreader)
    number_months= len(data)


#number_months = sum(1 for row in csvreader)-1

print (number_months)

#Split data in the first column
#Len function to count the months?

#The net total amount of "Profit/Losses" over the entire period

#Sum 2nd column
#$ sign addition

#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes

#Not Sure what that means

#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period
#In addition, your final script should both print the analysis to the terminal and export a text file with the results.

##Text file with the results?

 # Total matches can be found by adding wins, losses, and draws together
    total_matches = wins + losses + draws

    # Win percent can be found by dividing the the total wins by the total matches and multiplying by 100
    win_percent = (wins / total_matches) * 100

    # Loss percent can be found by dividing the total losses by the total matches and multiplying by 100
    loss_percent = (losses / total_matches) * 100

    # Draw percent can be found by dividing the total draws by the total matches and multiplying by 100
    draw_percent = (draws / total_matches) * 100

    # If the loss percentage is over 50, type_of_wrestler is "Jobber". Otherwise it is "Superstar".
    if loss_percent > 50:
        type_of_wrestler = "Jobber"
    else:
        type_of_wrestler = "Superstar"

    # Print out the wrestler's name and their percentage stats
    print(f"Stats for {name}")
    print(f"WIN PERCENT: {win_percent}")
    print(f"LOSS PERCENT: {loss_percent}")
    print(f"DRAW PERCENT: {draw_percent}")
    print(f"{name} is a {type_of_wrestler}")


# Read in the CSV file
with open(wrestling_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    # Prompt the user for what wrestler they would like to search for
    name_to_check = input("What wrestler do you want to look for? ")

    # Loop through the data
    for row in csvreader:

        # If the wrestler's name in a row is equal to that which the user input, run the 'print_percentages()' function
        if name_to_check == row[0]:
            print_percentages(row)

