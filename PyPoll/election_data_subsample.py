import os
import csv

IN_PATH = os.path.join("Analysis", "election_data.csv")
OUT_PATH = os.path.join("subset.csv")

rows = 0

with open(IN_PATH, "r") as in_file, open(OUT_PATH, "w+") as out_file: 
    
    reader = csv.reader(in_file)
    header = next(reader)

    writer = csv.writer(out_file)
    writer.writerow(header)
    count = 0
    
    for row in reader:
        count += 1
        if count < 1000:
            writer.writerow(row)
        
        
            
        
            
    
    

    