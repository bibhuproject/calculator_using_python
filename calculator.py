from tkinter import *
root = Tk()
root.title("calculator")
def add():
    if not t1.get() and not t2.get():
        print("Please enter a number")
    else:
        res=int(t1.get())+int(t2.get())
        lbl_text.config(text = "RESULT =%d" % (res))
        t1.set=""
        t2.set=""
def sub():
    if not t1.get() and not t2.get():
        print("Please enter a number")
    else:
        res=int(t1.get())-int(t2.get())
        lbl_text.config(text = "RESULT =%d" % (res))
        t1.set=""
        t2.set=""
def mul():
    if not t1.get() and not t2.get():
        print("Please enter a number")
    else:
        res=int(t1.get())*int(t2.get())
        lbl_text.config(text = "RESULT =%d" % (res))
        t1.set=""
        t2.set=""
def div():
    if not t1.get() and not t2.get():
        print("Please enter a number")
    else:
        res=int(t1.get())/int(t2.get())
        lbl_text.config(text = "RESULT =%d" % (res))
        t1.set=""
        t2.set=""
l1=Label(root,text="Enter First Number:",font=("Ariel",14))
t1=Entry(root)
l2=Label(root,text="Enter First Number:",font=("Ariel",14))
t2=Entry(root)
lbl_text = Label()
lbl_text.place(x=350,y=130)
b1=Button(root,text = "sum",fg='white',bg='blue',command=add)
b2=Button(root,text = "Diffrence",fg='white',bg='blue',command=sub)
b3=Button(root,text = "product",fg='white',bg='blue',command=mul)
b4=Button(root,text = "Divide",fg='white',bg='blue',command=div)
b5=Button(root,text = "Cancel",fg='white',bg='blue')

l1.place(x=50,y=50)
l2.place(x=50,y=100)
t1.place(x=350,y=50)
t2.place(x=350,y=100)

b1.place(x=70,y=150)
b2.place(x=140,y=150)
b3.place(x=250,y=150)
b4.place(x=350,y=150)
b5.place(x=440,y=150)
root.mainloop()
