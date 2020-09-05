import os
import csv

IN_PATH = os.path.join("subset.csv")
OUT_PATH = os.path.join("Analysis", "election_data_analysis.txt")



with open(IN_PATH, 'r') as in_file:
    
    reader = csv.reader(in_file)
    header = next(reader)
    
    retrieve_cand = []
    khan = []
    corry = []
    li = []
    otooley = []
    
    for row in reader:
        retrieve_cand.append(row[2])
        
    cand_name_count = []
    cand_name_count = dict(name)
        
    for x , y in retrieve_cand:
        if 
        
    for row in retrieve_cand:
        if row == "Khan":
            khan.append(row)
            k_vote = len(khan)
        elif row == "Correy":
            corry.append(row)
            c_vote = len(corry)
        elif row == "Li":
            li.append(row)
            l_vote = len(li)
        else:
            otooley.append(row)
            o_vote = len(otooley)
     
    total_vote = k_vote + c_vote + l_vote + o_vote
    average_k = round((k_vote / total_vote), 2) 
    average_c = round((c_vote / total_vote), 2)
    average_l = round((l_vote / total_vote), 2)
    average_o = round((o_vote / total_vote), 2)
        
    

print(total_vote)
print(average_c)
print(average_k)
print(average_l)
print(average_o)

   
data = [
["Edward", 123],
["Doug", 123123],
["Edward", 2432],
["Edward", 2432],
["Umair", 345],
["Edward", 2432]
]
results = {}
for candidate, votes in data:
    if candidate in results:
        results[candidate] += votes
    else:
        results[candidate] = votes
    
    print(50  * "=")
    print(results)
print(50  * "=")
print(results)        
     
        
