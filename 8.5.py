
fh = open("mbox-short.txt.txt")
count=0
for line in fh:
    if line.startswith ("From"):
        if line.startswith ("From:"):
            continue
        count+=1
        emails=line.split()
        email=emails[1]
        print (email)

print("There were", count, "lines in the file with From as the first word")