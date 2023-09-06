import os
import csv

budget_path = os.path.join("Resources", "budget_data.csv")

date = []
changes = []
with open(budget_path, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    Hearder = next(csv_reader,None)
    totalmonths = 0
    totalvalue = 0
    start_value = None

    for row in csv_reader:
        totalmonths += 1
        if totalmonths == 1:
            first_value = int(row[1])

        totalvalue = int(row[1]) + totalvalue
        last_value = int(row[1])

        if start_value is not None:
            change = last_value - start_value
            changes.append(change)
            date.append(row[0])
        start_value = last_value

    average = (last_value - first_value ) / (totalmonths - 1 )
    average = round(average, 2)


    clean_csv = list(zip(date, changes))

    greatest_increase = []    
    greatest_decrease = []
    greatest_increase = [row for row in clean_csv if row[1] == max(changes)]
    greatest_decrease = [row for row in clean_csv if row[1] == min(changes)]

    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: " + str(totalmonths))
    print(f"Total: $" + str(totalvalue))
    print(f"Average Change: $" + str(average))
    print(f"Greatest Increase in Profits: " + greatest_increase[0][0] +  " ($"+ str(greatest_increase[0][1]) + ")")
    print(f"Greatest Decrease in Profits: " + greatest_decrease[0][0] +  " ($"+ str(greatest_decrease[0][1]) + ")")
     


output_path = os.path.join("analysis", "output.txt")
with open(output_path, "w", newline='') as datafile:
    csv_writer = csv.writer(datafile)
    csv_writer.writerow(["Financial Analysis"])
    csv_writer.writerow(["----------------------------"])
    csv_writer.writerow(["Total Months: " + str(totalmonths)])
    csv_writer.writerow(["Total: $" + str(totalvalue)])
    csv_writer.writerow(["Average Change: $" + str(average)])
    csv_writer.writerow(["Greatest Increase in Profits: " + greatest_increase[0][0] +  " ($"+ str(greatest_increase[0][1]) + ")"])
    csv_writer.writerow(["Greatest Decrease in Profits: " + greatest_decrease[0][0] +  " ($"+ str(greatest_decrease[0][1]) + ")"])
