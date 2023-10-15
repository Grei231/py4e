# 5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. 
# If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match 
# the output below.


largest = None
smallest = None

# creating an empty list
nums = [] 
        
while True:
    snum = input("Enter a number: ")
    if snum == "done":
        break
    try:
        num=int(snum)
        ele = num
        # adding the element
        nums.append(ele) 
    except:
        print ("Invalid input")
        continue


#find largest
for num in nums: 
    if largest is None:
        largest = num
    elif num>largest:
        largest=num 
 

#find smallest
for num in nums: 
    if smallest is None:
        smallest = num
    elif num<smallest:
        smallest=num 
 
#print(nums)
print("Maximum is", largest)
print("Minimum is", smallest)

