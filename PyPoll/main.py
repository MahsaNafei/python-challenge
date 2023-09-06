import os
import csv

election_path = os.path.join("Resources", "election_data.csv")

candidate_name = []
candidate_info = {}

with open(election_path, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    Hearder = next(csv_reader)
    total_votes = 0

    for row in csv_reader:
        total_votes += 1
        candidate = row[2]

        if candidate in candidate_info:
            candidate_info[candidate]['votes'] += 1
            
        else:
            candidate_name.append(candidate)
            candidate_info[candidate] = {'votes': 1, 'percentage': 0}                   

for candidate, value in candidate_info.items():
    percent = (value['votes'] / total_votes) * 100
    percent = round(percent, 3)
    candidate_info[candidate]['percentage'] = percent

winner = [candidate for candidate, value in candidate_info.items() if value['votes'] == max(value['votes'] for value in candidate_info.values())]


print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate in candidate_name:
    print(f"{candidate}: {candidate_info[candidate]['percentage']}% ({candidate_info[candidate]['votes']})")
print("-------------------------")
print(f"Winner: {winner[0]}")
print("-------------------------")
    

output_path = os.path.join("analysis", "output.txt")
with open(output_path, "w", newline='') as datafile:
    csv_writer = csv.writer(datafile)
    csv_writer.writerow(["Election Results"])
    csv_writer.writerow(["-------------------------"])
    csv_writer.writerow([f"Total Votes: {total_votes}"])
    csv_writer.writerow(["-------------------------"])
    csv_writer.writerow([""])
    for candidate in candidate_name:
        csv_writer.writerow([f"{candidate}: {candidate_info[candidate]['percentage']}% ({candidate_info[candidate]['votes']})"])
    csv_writer.writerow(["-------------------------"])
    csv_writer.writerow([f"Winner:  {winner[0]}"])
    csv_writer.writerow(["-------------------------"])