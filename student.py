import tkinter as tk
root=tk.Tk()
root.geometry('2000x900')
root.title("my application")
root.config(bg='light green')
m1=tk.Label(root,text="welcome to my new application",font=("Algerian",20,"bold"))
m1.place(x=500,y=50)
m2=tk.Label(root,text="LOGIN PAGE",font=("Algerian",18,"bold"))
m2.place(x=600,y=100)
m3=tk.Label(root,text="USER NAME",font=("Arial black",18,"bold"))
m3.place(x=500,y=200)
e1=tk.Entry(root,font=("arial",16))
e1.place(x=700,y=200)
m4=tk.Label(root,text="PASSWORD",font=("arial black",18,"bold"))
m4.place(x=500,y=300)
e2=tk.Entry(root,font=("arial black",16))
e2.place(x=700,y=300)
b1=tk.Button(root,text="LOGIN",font=("arial",16))
b1.place(x=600,y=400)
b2=tk.Label(root,text="Signup",font=("arial",16))
b2.place(x=700,y=400)
root.mainloop()