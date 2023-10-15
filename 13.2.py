#Extracting Data from JSON
#In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py. 
#The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment 
#counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:

import urllib.request
import json

# Prompt for the URL
url = "http://py4e-data.dr-chuck.net/comments_1899081.json"

try:
    # Open the URL and read the data
    response = urllib.request.urlopen(url)
    data = response.read().decode()

    # Parse the JSON data
    json_data = json.loads(data)

    # Extract the comment counts
    comment_counts = [item["count"] for item in json_data["comments"]]

    # Calculate the sum of comment counts
    total_comments = sum(comment_counts)

    print(f"Total comment counts: {total_comments}")
except Exception as e:
    print("An error occurred:", str(e))
