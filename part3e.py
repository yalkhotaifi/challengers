import re
p= input("Input your password")
x = True
count = 0
if(len(p)>7):
    for i in range(len(p)): 
if re.search("[0-9]",p):
    count += 1
if re.search("[!@#$%^&*]",p):
    count += 1

if(count >= 2):
    print("Valid Password")
    x = False
if x:
    print("Not a Valid Password")
