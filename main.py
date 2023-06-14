import random
import string
import time
import webbrowser
string.ascii_letters

user= int(input("how many loops"))

for i in range(user):
    x= random.choice(string.ascii_letters)
    y= random.choice(string.ascii_letters)
    a= random.randrange(0,9)
    b= random.randrange(0,9)
    c= random.randrange(0,9)
    d= random.randrange(0,9)
    f=("https://prnt.sc/"+ str(x.lower()+y.lower())+ str(int(a,))+str(int(b))+str(int(c))+str(int(d)) )
    time.sleep(.5)
    webbrowser.open(f)



#print(f)