#Question 1
print("Solution of Question 1")
string = input("Enter a string: ").lower()
#convert to list for counting words
stringlist = string.split()
def count_in_dict(list):
    count = {}
    n = len(list)
    for i in range(n):
        if list[i] in count:
            count[list[i]] += 1
        else:
            count[list[i]] = 1
    return count
#check for number of words
if len(stringlist) == 1:
    
    #making a list of all the letters
    stringlist = list(stringlist[0])
    print(count_in_dict(stringlist))
else:
    # the list has more than one word
    # so the function will count the words
    
    print(count_in_dict(stringlist))
print(" ")


#Question 2 (To print the next input date)
print("Solution of Question 2")
day=int(input("Enter the DAY:"))
month=int(input("Enter the month:"))
year=int(input("Enter the year:"))
if 1<=day and day<=31 and 1<=month and month<= 12 and 1800<=year<=2025 and not((day==31 and(month==2 or month==4 or month==6 or month==9 or month==11)) or (day==30 and month==2) or (year%4!=0 and day==29 and month==2)):
    new_day=day+1
    new_month=month
    new_year=year
    if day==31 and (month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12):
        new_day=1
        new_month=month+1
    #Month having 30 day
    if day==30 and (month==4 or month==6 or month==9 or month==11):
        new_day=1
        new_month=month+1
    #Month having 29 day 
    if (month==2 and day==29 and year%4==0) or month==2 and day==28 and year%4!=0:
        new_day=1
        new_month=month+1
    
    if month==12:
        new_year=1
        new_year=year+1
    if (year%4==0 and month==2 and day==29):
        new_day=1
        new_month=3
    print("The next date is : ",new_day,"/",new_month,"/",new_year)
else:
    print("Entered Date is not correct.")
print(" ")        

#Question 3(Create a lists of tuples with first element as the number and second element as the square of the number)
print("Solution of Question 3")
list=[]
element=int(input("Enter how many number you want to add in the list of tuples:"))
for i in range(0,element):
    elements=int(input("Enter the element="))
    list.append(elements)
a=[(x,x**2) for x in (list)]
print(a)
print(" ")

#Question 4(To print the grade and the performance entered by the user)
print("Solution of Question 4")
grade=int(input("Enter the GRADE points of the students:"))
if grade==4:
    print("Your Grade is 'D' and Poor Performance")
elif grade==5:
    print("Your Grade is 'C' and Below Average Performance")
elif grade==6:
    print("Your Grade is 'C+' and Average Performance")
elif grade==7:
    print("Your Grade is 'B' and Good Performance")
elif grade==8:
    print("Your Grade is 'B+' and Very GoodPerformance")
elif grade==9:
    print("Your Grade is 'A' and Excellent Performance")
elif grade==10:
    print("Your Grade is 'A+' and Outstanding Performance")
else:
    print("You have ENTERED GRADE out of range")
print(" ")

#Question 5 (Code to print the following pattern)
print("Solution of Question 5")
n = 6
for i in range(n):
    # printing spaces
    for j in range(i):
        print(' ', end='')
    # printing alphabet
    for j in range(2*(n-i)-1):
        print(chr(65 + j), end='')
    print()
print(" ")

#Question 6
print("Solution of Question 6")
sid = int(input("Enter SID: "))
name = input("Enter Name: ")
students = {sid:name}
while True:
    option = input("Do you want to enter another student entry(Y or N):").upper()
    if option == 'Y':
        sid = int(input("Enter SID: "))
        name = input("Enter Name: ")
        students[sid] = name
    elif option == 'N':
        break
    else:
        print('Invalid input!')
#part a. print the dictionary
print("a.",students)
#part b. sort acc to the names
print("b.",{k:v for k,v in sorted(students.items(), key= lambda x:x[1])})
#part c. sort acc to the SIDs
print("c.",{k:v for k,v in sorted(students.items())})
#part d. search for a student by their SID
sid = int(input("Search Name with SID: "))
print("d.",students[sid])
print(" ")

#Question 7(Python program to print the fibonacci series and take its averages)
print("Solution of Question 7")
terms = int(input("Upto which number terms you want to print fibonacci series="))
list=[]

n1, n2 = 0, 1
count = 0

# Checking integers
if terms <= 0:
   print("Please Enter a positive integer")
# Condition for only one term
elif terms == 1:
   print("Fibonacci sequence upto",terms,":")
   print(n1)
# Printing Fibonacci Series
else:
   print("Fibonacci sequence are as follows:")
   while count < terms:
       print(n1)
       list.append(n1)
       nth = n1 + n2
     # Updating values in the Fibonacci series
       n1 = n2
       n2 = nth
       count += 1
# Taking average of Fibonacci series
b=sum(list)/len(list)
print("The average of the Fibonacci series=",b)
print(" ")


#Question 8
print("Solution of Question 8")
set1={1,2,3,4,5}
set2={2,4,6,8}
set3={1,5,9,13,17}
print("Part (a)")
set_a=(set1 | set2) -(set1& set2)
print(set_a)
print("Part (b)")
set_b=(set1 | set2 | set3) -(set1& set2)-(set3&set1)
print(set_b)
print("Part (c)")
set_c=(set1& set2)|(set2&set3)|(set3&set1)-(set1 & set2 & set3)
print(set_c)
print("Part (d)")
list_d=[]
for i in set1:
    if i>=1 and i<=10:
        list_d.append(i)
set_d=set(list_d)
print( set_d)
print("Part (e)")
list_e=[]
for i in (set1 | set2 | set3):
     if i>=1 and i<=10:
        list_e.append(i)
set_eout=set(list_e)
print(set_eout)
print(" ")
print("********************************THE END********************************")
    




