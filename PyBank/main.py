import os
import csv

OUT_PATH = os.path.join("Analysis","budget_data_analysis.txt")
path = os.path.join("Resources", "budget_data.csv")

with open(path, "r") as in_file, open(OUT_PATH, "w+") as out_file:
    
    csv_reader = csv.DictReader(in_file)
    
    reader_data = list(csv_reader)
      
    change = []
    total_mon = 0
    total = 0
    great_incr = 0
    great_decr = 0
    great_incr_date = 0
    great_decr_date = 0

    for i in range(1, len(reader_data)):

        last_period_row = reader_data[i - 1]
        current_period_row = reader_data[i]
        
        total_mon = i + 1
        total += int(current_period_row["Profit/Losses"])
        
        changes = int(current_period_row["Profit/Losses"]) - int(last_period_row["Profit/Losses"])
        change.append(changes)
        
        if changes > great_incr:
            great_incr = changes
            great_incr_date = current_period_row["Date"]
            
        if changes < great_decr:
            great_decr = changes
            great_decr_date = current_period_row["Date"]
            
    average_change = round(sum(change) / len(change), 2)

    output_txt = f"Financial Analysis\n"\
    f"------------------------------------------------------------------\n"\
    f"Total Months:                   {total_mon}\n"\
    f"Total:                          ${total}\n"\
    f"Average Change:                 ${average_change}\n"\
    f"Greatest Increase in Profits:   {great_incr_date} (${great_incr}) \n"\
    f"Greatest Decrease in Profits:   {great_decr_date} (${great_decr})\n"\

    print(output_txt)
    out_file.write(output_txt)
    
    