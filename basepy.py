import tkinter as tk

window =  tk.Tk()
window.geometry("500x500+1000+200")
window.bind("<q>",lambda e: window.quit())
window.maxsize(500,500)

string = tk.StringVar()
cal = ""
def calculate():
    global cal
    try:
        cal = entry.get()
        if " x " in cal:
            cal = cal.replace("x","*")
        if " : " in cal:
            cal = cal.replace(":","/")
        string.set(eval(cal))
    except Exception as e:
        string.set(e)

def clear():
    global cal
    cal = ""
    string.set(cal)

def input(val):
    global cal
    cal = entry.get()
    cal += str(val)
    string.set(cal)


frame_outp = tk.Frame(window,bd=0,bg="white",highlightbackground="black",highlightcolor="purple",highlightthickness=2)
entry = tk.Entry(frame_outp,fg="blue",font=("arial",13,"bold"),textvariable=string,justify="right",selectbackground="yellow",selectborderwidth=2,selectforeground="green")
entry.pack(ipady=10,fill="both",expand=True)
frame_outp.pack(side="top",fill="both")

button = [("1",0,0),("2",0,1),("3",0,2),("4",0,3),("5",1,0),("6",1,1),("7",1,2),("8",1,3),("9",2,0),("0",2,1),("=",3,1),("C",3,0),(" + ",2,2),(" - ",2,3),(" x ",3,2),(" : ",3,3)]
frame_inp = tk.Frame(window)
frame_inp.pack(pady=10)

    
for val,row,col in button:
    if val == "=":
        btn = tk.Button(frame_inp,text=val,width=10,height=3,bd=1,bg="grey",cursor="arrow",command= calculate)
    elif val == "C":
        btn = tk.Button(frame_inp,text=val,width=10,height=3,bd=1,bg="orange",cursor="hand2",command= clear)
    else:
        btn = tk.Button(frame_inp,text=val,width=10,height=3,bd=1,bg="white",cursor="hand2",command= lambda te=val:input(te))
    btn.grid(row=row,column=col,padx=2,pady=2)
window.mainloop()