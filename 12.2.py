#Scraping Numbers from HTML using BeautifulSoup In this assignment you will write a Python program 
#The program will use urllib to read the HTML from the data files below, and parse the data, extracting numbers and 
#compute the sum of the numbers in the file.
#You are to find all the <span> tags in the file and pull out the numbers from the tag and sum the numbers.

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_1899078.html"
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the span  tags
tags = soup('span')
sum = 0
for tag in tags:
    # Look at the parts of a tag
    #print('TAG:', tag)
    #print('URL:', tag.get('href', None))
    #print('Contents:', tag.contents[0])
    #print('Attrs:', tag.attrs)
    num=tag.contents
    for el in num:
        fnum=float(el)
        sum=sum+fnum

print (int(sum))


    