
from csv import DictReader
import csv
from datetime import datetime

now = datetime.now()

print(now.hour)

# open file in read mode
with open("stats.csv", 'r') as f:
    dict_reader = DictReader(f)
    list_of_dict = list(dict_reader)



tmp = int(list_of_dict[now.hour]["[Antal]"])
tmp += 1
list_of_dict[now.hour]["[Antal]"] = tmp

print(list_of_dict[now.hour]) 

with open("stats.csv", 'w') as f:
    # creating a csv dict writer object 
    writer = csv.DictWriter(f, fieldnames = ['[Tid]', '[Antal]']) 
        
    # writing headers (field names) 
    writer.writeheader() 
        
    # writing data rows    
    writer.writerows(list_of_dict) 