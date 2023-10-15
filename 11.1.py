# In this assignment you will read through and parse a file with text and numbers. 
# You will extract all the numbers in the file and compute the sum of the numbers.

import re 

handle = open ("actual.txt")

sum = 0

for line in handle:
    num=re.findall("[0-9]+",line)
    for item in num:
        fl=float (item)
        sum = sum + fl 

print (int(sum))