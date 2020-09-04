import os
import csv

IN_PATH = os.path.join("Resources", "election_data.csv")
OUT_PATH = os.path.join("Analysis", "election_data_analysis.txt")

with open(IN_PATH, "r") as in_file, open(OUT_PATH, "w+") as out_file:
    
    reader = csv.DictReader(in_file)
    
    data = list(reader)
    
