import os
import csv

IN_PATH = os.path.join("Resources", "election_data.csv")
OUT_PATH = os.path.join("Analysis", "election_data_analysis.txt")



with open(IN_PATH, 'r') as in_file:
    
    reader = csv.reader(in_file)
    header = next(reader)
    
    retrieve_cand = []
    total_votes = 0

    for row in reader:
        retrieve_cand.append(row[2])
        
    cand_name_count = dict((name, retrieve_cand.count(name)) for name in set(retrieve_cand)) 
    
    v = list(cand_name_count.values())
    k = list(cand_name_count.keys())
    winner = k[v.index(max(v))] 
    
       
    for x, y in cand_name_count.items():
        
        total_votes += y
        
        if x == "Khan":
            k_vote = y
            average_k = round((y / total_votes), 2)
        elif x == "Correy":
            c_vote = y
        elif x == "Li":
            l_vote = y
        else:
            o_vote = y
        
    average_k = round((k_vote / total_votes)*100, 2)
    average_c = round((c_vote / total_votes)*100, 2)
    average_l = round((l_vote / total_votes)*100, 2)
    average_o = round((o_vote / total_votes)*100, 2)
        
output_text = f"Election Results \n"\
f"---------------------------------------------------\n"\
f"Total Votes: {total_votes}\n"\
f"---------------------------------------------------\n"\
f"Precent votes for Khan: {average_k}% ({k_vote}) \n"\
f"Precent votes for Correy: {average_c}% ({c_vote})\n"\
f"Precent votes for Li: {average_l}% ({l_vote})\n"\
f"Precent votes for O'Tooley: {average_o}% ({o_vote})\n"\
f"---------------------------------------------------\n"\
f"Election Winner: {winner}\n"\
f"---------------------------------------------------\n"\

print(output_text)
with open(OUT_PATH, "+w") as out_file:
    out_file.write(output_text)
 