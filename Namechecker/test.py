temp = "D\df\df\dsfss\sdf\kum.txt"
temp1 = "dkj.txt"

def splitter(path):
    if "\\" in path:
      x = path.split("\\")
      S = (x[len(x)-1])
      return S
    else:
        return path

print(splitter(temp))
print(splitter(temp1))

from tkinter import *
from functools import partial

def validateLogin(username, password):
	print("username entered :", username.get())
	print("password entered :", password.get())
	return

#window
tkWindow = Tk()
tkWindow.geometry('400x150')
tkWindow.title('Tkinter Login Form - pythonexamples.org')

#username label and text entry box
usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)

#password label and password entry box
passwordLabel = Label(tkWindow,text="Password").grid(row=1, column=0)
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)

validateLogin = partial(validateLogin, username, password)

#login button
loginButton = Button(tkWindow, text="Login", command= ).grid(row=4, column=0)

tkWindow.mainloop()