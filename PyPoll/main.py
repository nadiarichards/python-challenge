import os
import csv

election_csv = os.path.join('Resources', 'election_data.csv')
file_output = os.path.join('Analysis', 'election_analysis.txt')

total_votes=0
candidate_options = []
candidate_voter_count={}
voter_percent={}

with open(election_csv) as csvfile:

    csvreader = csv.reader(csvfile)
    header=next(csvreader)
    first_row=next(csvreader)
    total_votes+=1

    for row in csvreader:

        total_votes+=1
        candidate_names=row[2]

        if candidate_names not in candidate_options:
            candidate_options.append(candidate_names)
            candidate_voter_count[candidate_names] = 0

        candidate_voter_count[candidate_names] += 1

winning_candidate = max(candidate_voter_count, key=candidate_voter_count.get)

for i in candidate_voter_count:
    voter_percent[i]=(float(candidate_voter_count[i]/total_votes)*100)

with open(file_output,"w") as txt_file:

    election_results=(
        f"Election Results\n"
        f"__________________________\n"
        f"Total Votes: {total_votes}\n"
        f"__________________________\n")
    print(election_results, end="")
    txt_file.write(election_results)

    for candidate_name in candidate_voter_count:
        votes=candidate_voter_count.get(candidate_name)
        percent=voter_percent.get(candidate_name)
        candidate_summary=(
            f"{candidate_name}: {percent:.3f}% ({votes})\n")
        print(candidate_summary)
        txt_file.write(candidate_summary)

    winning_summary=(
        f"__________________________\n"
        f"Winner: {winning_candidate}\n"
        f"__________________________\n")
    print(winning_summary)
    txt_file.write(winning_summary)