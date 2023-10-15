#Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
#The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
#The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
#After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

import matplotlib.pyplot as plt

handle = open("mbox-short.txt.txt") #open file

counts=dict() #create empty dict

for line in handle:
    if line.startswith ("From"):
        if line.startswith ("From:"):
            continue
        emails=line.split()
        email=emails[1]
        #print (email)
        counts[email]=counts.get(email,0)+1

#print (counts)

bigcount=None
bigemail=None
for email,count in counts.items():
    if bigcount is None or count>bigcount:
        bigemail=email
        bigcount=count

print (bigemail,bigcount)







# Create lists for email addresses and corresponding message counts
email_addresses = list(counts.keys())
message_counts = list(counts.values())

# Create a histogram
plt.bar(email_addresses, message_counts)
plt.xlabel('Email Addresses')
plt.ylabel('Message Counts')
plt.title('Email Message Counts by Sender')
plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
plt.tight_layout()

# Show the histogram
plt.show()
