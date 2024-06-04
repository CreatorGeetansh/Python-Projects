n = input("enter: ")
import random as ran
import string as str
import time as ti

if(len(n)==3):
    print(f"{n[2] + n[1] + n[0]}")
elif(len(n)==2):
    print(f"{n[1]+n[0]}")
elif(len(n) == 1):
    print(f"{n[0]}")
y = n[::-1]
r1 = ran.choice(str.ascii_letters) + ran.choice(str.ascii_letters) + ran.choice(str.ascii_letters) 
  #this random choice is function which allows the program to choose random values for the data filled inside the bracket
  #just like string.ascii_letters isse ham sare alphabets to access kr skte h and random keyword hame randomly choose krwata h
r2 = ran.choice(str.ascii_letters) + ran.choice(str.ascii_letters) + ran.choice(str.ascii_letters)
print(f"{r1 + y + r2}")

z = input("Enter for decrption: ") 
if(len(z)==3):
   print(f"{z[2]+z[1]+z[0]}")
elif(len(z)==2):
   print(f"{z[1]+z[0]}")
elif(len(z) == 1):
   print(f"{z[0]}")
else: 
   x = z[3:len(z)-4]
   b = x[::-1]
   print(f"{z[len(z)-4] + b}")
ti.sleep(4)