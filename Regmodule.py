import csv 
import re

"""
So regular expression is used to check the different combination of strings that can be possible 
e.g. :- THE OFFICE, The OFfice, the OFFICE, the office, ThE OffICE, etc..

A regular expression (or RE) specifies a set of strings that matches it; the functions in this module let you check if a particular string matches a given regular expression (or if a given regular expression matches a particular string, which comes down to the same thing).

"""


count=0
with open('smaple.csv',"r") as file:
    read=csv.DictReader(file)
    for row in read:
        a=row['title'].strip().upper()

        #Here we used the search function with re module we are searching ^ means check at the start for OFFICE | means or     The.OFFICE (.) means check for any number/string etc  $ means at last
        if re.search("^(OFFICE|THE.OFFICE)$",a):
            count+=1
print("People who liked ther series :-OFFICE",count)




