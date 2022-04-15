# https://www.youtube.com/watch?v=D-1kNFO568c&t=2012s

import csv
from itertools import count 
import re

count=0
a=input("Enter you favourite TV SHOW:-").upper()
with open('smaple.csv','r') as ste:
    readed=csv.DictReader(ste)
    for row in readed:
        title=row['title'].strip().upper()
        if re.search(f"(^.*{a}|.*{a}.+)$",title):
            count+=1

print(f"This number like:-{count}")