#Following Links in Python

#In this assignment you will write a Python program that expands on http://www.py4e.com/code3/urllinks.py. 
#The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, 
#scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat the process 
#a number of times and report the last name you find.

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url="http://py4e-data.dr-chuck.net/known_by_Molly.html"

# Function to retrieve the href values from the anchor tags in the HTML
def get_href_links(url):
    try:
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        tags = soup('a')
        href_links = [tag.get('href', None) for tag in tags]
        return href_links
    except:
        return None


# Main function to follow links and report the last name
def follow_links(url, position, repeat):
    current_url = url
    for i in range(repeat):
        href_links = get_href_links(current_url)
        if href_links is None or len(href_links) < position:
            print("Unable to retrieve or locate the link at position", position)
            break
        next_url = href_links[position-1]
        print("Retrieving:", next_url)
        current_url = next_url
    print("Last name found at position", position, "is:", current_url)



# Input parameters
position = int(input("Enter the position of the link to follow (1-based index): "))
repeat = int(input("Enter the number of times to repeat the process: "))


# Call the main function
follow_links(url, position, repeat)
    