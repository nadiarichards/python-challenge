import os
import csv

# Path to collect data from the Resources folder
election_csv = os.path.join('Resources', 'election_data.csv')
###file_output = os.path.join('Analysis', 'election_analysis.txt')

total_votes=0
candidate_options = []
candidate_voter_count={}
voter_percent={}
#candidates={}
#candidates=dict()
#greatest_increase=["",0]
#greatest_decrease=["",99999999999]
#total_net=0

#candidate_index=[]
maximum_votes=0

with open(election_csv) as csvfile:

    csvreader = csv.reader(csvfile)
    header=next(csvreader)
    first_row=next(csvreader)
    total_votes+=1
    #voter_percent = int(candidate_voter_count/ total_votes) * 100
    #total_net+=int(first_row[1])
    #previous_net=int(first_row[1])

    for row in csvreader:

        total_votes+=1
        candidate_names=row[2]

        if candidate_names not in candidate_options:
            candidate_options.append(candidate_names)
            print(candidate_names)
            candidate_voter_count[candidate_names] = 0

        # Count times Candidate name appears
        candidate_voter_count[candidate_names] += 1
print(total_votes)
print(candidate_voter_count)

maximum_votes = max(candidate_voter_count, key=candidate_voter_count.get)
print (maximum_votes)

#This works, but it shanges the original dictionary with percentage values. 
#Need to add an extra value with percentages to the dictionary.
#It also needs to only have 2 decimals after the . NOT ROUNDING CORRECTLY - 1 decimal
for i in candidate_voter_count:
    candidate_voter_count[i]=round(float((candidate_voter_count[i]/total_votes)*100),3)

print (candidate_voter_count)

#voter_percent=(candidate_voter_count/total_votes) *100
#print (voter_percent)
#Total_percentage=float(votes/float(total_votes)*100)

#if voter_percent == maximum_votes:
    #type_of_candidate = "Winner"
#else:
    #type_of_candidate = "Looser"


#candidate_voter_count=election_csv(row[2]).count(int(candidate_names)
            #candidate =[candidate for candidate in candidates]

        # for candidate in candidates:

        #     if row[2] == candidate:
        #         candidate_index = int(candidate) - 1
        #         candidate_voter_count[candidate_index] += 1
        #         for candidate_index in range(len(candidates)):
        #             candidate_count = str(candidate_voter_count[candidate_index])
        #             candidate_name = str(candidates[candidate_index])

        #             candidate_voter_count=Counter(candidates)


        #             for i in range(len(candidates)):
        #                 candidates[i]=candidates[i].count()

               
                    #    percent = round(int(row[6]) / int(row[5]), 2)
                    #     review_percent.append(percent)
                # candidate_voter_count=str()
                # candidate_voter_count+=1
                # candidate_voter_count.append(row[0])



#hot_days = [temperature for temperature in july_temperatures if temperature > 90]

# def average(numbers):
#     length = len(numbers)
#     total = 0.0
#     for number in numbers:
#         total += number
#     return total / length


# # Test your function with the following:
# print(average([1, 5, 9]))
# print(average(range(11)))

        #total_net+=int(row[1])
        #net_change=int(row[1])-previous_net
        #previous_net=int(row[1])
        #net_change_list+=[net_change]
        #months_of_change+=[row[0]]

#         if net_change > greatest_increase[1]:

#             greatest_increase[0]=row[0]
#             greatest_increase[1]=net_change

#         if net_change < greatest_decrease[1]:

#             greatest_decrease[0]=row[0]
#             greatest_decrease[1]=net_change

# net_monthly_average=sum(net_change_list)/len(net_change_list)

# output=(
#     f"Election Results\n"
#     f"----------------------------------\n"
#     f"Total Votes: {total_votes}\n"
#     f"----------------------------------\n"
#     f"Total: ${total_net}\n"
#     f"Average Change: ${net_monthly_average:.2f}\n" 
#     f"Greatest Increase in Profits:{greatest_increase[0]}(${greatest_increase[1]})\n"
#     f"Greatest Decrease in Profits:{greatest_decrease[0]}(${greatest_decrease[1]})\n"
# )

# print(output)

# with open(file_output,"w") as txt_file:
#     txt_file.write(output)