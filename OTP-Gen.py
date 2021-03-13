import random
from tkinter import messagebox
from tkinter import *

root = Tk()

#generate OTP
gen=random.randint(000000,100000)

username=input('Enter the username:')

print('hello',username)

#show the otp in dialog box
messagebox.showinfo("OTP",gen)
#print('Here is your OTP:',gen)

password=input("Enter the otp to login:")

#verify OTP and user input are equal or not
if password==str(gen):
    print('Login success')
else:
    password!=str(gen)
    print('login failed')


root.destroy()
