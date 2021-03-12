#C) Write a program containing a function to convert the current time, into military time

import datetime
time = ''
def timeConversion(currenrTime):
   if currenrTime[-2:] == "AM" :
      if currenrTime[:2] == '12':
          time = str('00' + currenrTime[2:8])
      else:
          time = currenrTime[:-2]
   else:
      if currenrTime[:2] == '12':
          time = currenrTime[:-2]
      else:
          time = str(int(currenrTime[:2])) + currenrTime[2:8]
   return time


currenrTime = datetime.datetime.now()
print("Current miliatry time:",timeConversion(currenrTime.strftime("%H%M")))

#D) Write a program containing a function to output the fibonacci sum up to a user inputted number

#displaying the Fibonacci sequence
nterms = int(input("How many terms? "))

n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       
       n1 = n2
       n2 = nth
       count += 1

