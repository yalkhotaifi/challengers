#Write a program containing a function to convert the current time, into military time

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

