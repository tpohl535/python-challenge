import os
import csv

IN_PATH = os.path.join("election_data_subsample.cvs")
OUT_PATH = os.path.join("Analysis", "election_data_analysis.txt")

with open(IN_PATH, "r") as in_file, open(OUT_PATH, "w+") as out_file:  
    
    reader = csv.reader(in_file)
    header = next(reader)
    

    count = 0
    
    for row in reader:
        
        count += 1
        
        
        
        
        
    # format print to example   
    output_txt = f"Election Results\n"\
    f"-------------------------\n"\
    f"Total Votes: {count}\n"\
    f"-------------------------\n"\
    f"Khan: \n"\
    f"Corry: \n"\
    f"Li: \n"\
    f"O'Tooley: \n"\
    
    print(count)
    