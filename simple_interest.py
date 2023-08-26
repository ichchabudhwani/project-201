from tkinter import *
window=Tk()

window.title('SIMPLE INTEREST CALCULATOR')
window.geometry("380x400")
window.configure(bg='lightpink')

# Python3 program to find simple interest
# principal amount, time and
# rate of interest taken from user.


def simple_interest():
    p=float(principal_entry.get())
    t=float(time_entry.get())
    r=float(rate_entry.get())
    i=(p*r*t)/100
    output_message=Label(result_frame,text="Interest in Rs."+str(p)+"at the rate of interest"+str(r)+"for"+str(t)+"years in Rs.",bg="grey",font=("calibri 12"),width=55)
    output_message.place(x=20,y=40)
    output_message.pack()
    result_frame.destroy()
    

heading_label=Label(window, text="SIMPLE INTEREST CALCULATOR", fg = "black", bg = "lightpink", font=("Calibri", 20),bd=5)
heading_label.place(x=50, y=20)

username=Entry(window,text="",bd=4,width=22)
username.place(x=30,y=20)

principal_label=Label(window,text="principle", fg = "black", bg = "lightpink", font=("Calibri", 12),bd=1)
principal_label.place(x=90, y=142)

principal_entry=Entry(window, text="", bd=2, width=22)
principal_entry.place(x=50, y=142)

rate_label=Label(window,text="rate",fg="black",bg="lightpink",font=("Calibri",12),bd=1)
rate_label.place(x=20,y=185)

rate_entry=Entry(window,text="",bd=2,width=22)
rate_entry.place(x=150,y=187)

time_label=Label(window,text="time",fg="black",bg="lightpink",font=("Calibri",12),bd=1)
time_label.place(x=20,y=185)

time_entry=Entry(window,text="",bd=2,width=22)
time_entry.place(x=220,y=189)

button=Button(window,text="calculate",fg="black",bg="cyan",bd=4,command=simple_interest)
button.place(x=20,y=250)

show_label = LabelFrame(window,text=" your result will be displyed here", bg = "grey", font=("Calibri", 12),width=55)
show_label.place(x=20,y=20)
show_label.pack()
result_frame=LabelFrame(show_label,text="result", bg = "grey", font=("Calibri", 12))
result_frame.pack(pady=20,padx=20)
result_frame.place(x=20,y=300)

mainloop()
