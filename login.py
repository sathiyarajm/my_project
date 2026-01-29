import tkinter as tk

def login():
    if user.get() == "admin" and pwd.get() == "1234":
        result.config(text="Login Successful")
    else:
        result.config(text="Login Failed")

root = tk.Tk()
root.title("Login")

user = tk.Entry(root)
pwd = tk.Entry(root, show="*")
tk.Label(root, text="Username").pack()
user.pack()
tk.Label(root, text="Password").pack()
pwd.pack()
tk.Button(root, text="Login", command=login).pack()
result = tk.Label(root)
result.pack()

root.mainloop()
# This code creates a simple login GUI using Tkinter.
# It checks if the username is "admin" and the password is "1234".