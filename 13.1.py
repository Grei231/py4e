#Extracting Data from XML
#In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py. 
#The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment 
#counts from the XML data, compute the sum of the numbers in the file.

import urllib.request
import xml.etree.ElementTree as ET

# Prompt the user for a URL
url = 'https://py4e-data.dr-chuck.net/comments_1899080.xml'

# Read the XML data from the URL using urllib
try:
    data = urllib.request.urlopen(url).read()
except:
    print('Invalid URL or unable to retrieve data from the URL.')
    quit()

# Parse the XML data
tree = ET.fromstring(data)

# Find all 'count' elements using XPath
counts = tree.findall('.//count')

# Initialize a variable to store the sum of counts
total = 0

# Iterate through 'count' elements and add their values to the total
for count in counts:
    total += int(count.text)

# Print the sum of counts
print('Sum:', total)
