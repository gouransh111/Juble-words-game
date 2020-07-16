from tkinter import *
i = 1
j = 0
root = Tk()
a = ["eelahntp","gvaua","noamg","ppleur","msoue"]
a1 = ["elephant","guava","mango","purple","mouse"]
def submit():
    global i
    global j
    if scvalue.get() ==  a1[i-1]:
           #print(scvalue.get()) 
           check.set("Correct")
           j += 1 
    else:
        #print(scvalue.get())
        check.set("Wrong") 
    if i >= 5 and j > 4:
        win_label = Label(root,text="You Won",bg="purple",fg="red",font ="Arial 20 italic")
        win_label.pack(side=BOTTOM)
    elif i >= 5 and j<=4:
         win_label = Label(root,text="You Loss",bg="purple",fg="red",font ="Arial 20 italic")
         win_label.pack(side=BOTTOM) 
         win2 = Label(root,text = f"You give {4-j} wrong answer").pack(side=BOTTOM)   
    if i<5:
       jumbleword.set(f"{i+1}.{a[i]}")
       scvalue.set("") 
    i += 1
      
    #if i > 5: 
    #import time 
    #time.sleep(4)
    #quit()   
root.title("Jumble words")
root.configure(bg="black")
root.geometry("400x400")
scvalue = StringVar()
scvalue.set("")

jumbleword=StringVar()
jumbleword.set(f"{i}.{a[0]}")

f1 = Frame(root,borderwidth=8,relief=SUNKEN,bg = "green")
f1.pack(side=TOP,pady=30,padx=30,fill="x")

jumble = Label(f1,textvariable=jumbleword,fg="black",font = "Arial 10 bold").pack(side=TOP,pady=12)

jumblesentry = Entry(f1,textvar=scvalue,font= "lucida 13 bold")
jumblesentry.pack(side=BOTTOM,pady=22)

Submit = Button(root,text="Submit",fg="cyan",bg="purple",command=submit).pack()

check = StringVar() 
check.set("")         
lab = Label(root,textvar=check,font="lucida 10 underline",relief=SUNKEN)
lab.pack(side=BOTTOM,anchor="se")
root.mainloop()
