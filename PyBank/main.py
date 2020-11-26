import os
import csv

# Path to collect data from the Resources folder
budget_csv = os.path.join('Resources', 'budget_data.csv')
file_output = os.path.join('Analysis', 'budget_analysis.txt')

#The total number of months included in the dataset
# Name first and 2nd column
# Define the function 
    # For readability, it can help to assign your values to variables with descriptive names
total_months=0
months_of_change=[]
net_change_list=[]
greatest_increase=["",0]
greatest_decrease=["",99999999999]
total_net=0

with open(budget_csv) as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile)
    header=next(csvreader)
    first_row=next(csvreader)
    total_months+=1
    total_net+=int(first_row[1])
    previous_net=int(first_row[1])

    for row in csvreader:

        total_months+=1
        total_net+=int(row[1])
        net_change=int(row[1])-previous_net
        previous_net=int(row[1])
        net_change_list+=[net_change]
        months_of_change+=[row[0]]

        if net_change > greatest_increase[1]:

            greatest_increase[0]=row[0]
            greatest_increase[1]=net_change

        if net_change < greatest_decrease[1]:

            greatest_decrease[0]=row[0]
            greatest_decrease[1]=net_change

net_monthly_average=sum(net_change_list)/len(net_change_list)

output=(
    f"Financial Analysis\n"
    f"----------------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${net_monthly_average:.2f}\n" 
    f"Greatest Increase in Profits:{greatest_increase[0]}(${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits:{greatest_decrease[0]}(${greatest_decrease[1]})\n"
)

print(output)

with open(file_output,"w") as txt_file:
    txt_file.write(output)