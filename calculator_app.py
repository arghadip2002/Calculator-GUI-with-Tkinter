import customtkinter
from tkinter import *
from tkinter import messagebox

app = customtkinter.CTk()
app.title("Calculator")
app.geometry("250x270")
app.maxsize(250,270)
app.minsize(250,270)

app.config(bg="#000000")

font1= ("Arial", 20, "bold")

i=0
equation=""

def show(value):
    global i
    global equation
    if(value=="%"):
        value = "/100"
    equation+=value
    result_entry.insert(i,value)
    i+=1

def clear():
    global equation
    result_entry.delete(0,END)
    equation=""


def calculate():
    try:
        global equation
        result=""
        result=eval(equation)
        clear()
        result_entry.insert(0,result)
    except:
        messagebox.showerror(title="Error", message="Please Enter a valid number.")

result_entry = customtkinter.CTkEntry(app,placeholder_text="",font=font1,width=230,fg_color="black",border_color="white", height=40)
result_entry.place(x=10,y=10)



Button1 = customtkinter.CTkButton(app,command=clear,text="Clear",font=font1,width=110,height=20,fg_color="#FF6619",hover_color="#FF4219")
Button1.place(x=10,y=60)

Button3 = customtkinter.CTkButton(app,command=lambda:show("%"),text="%",font=font1,width=50,height=20,fg_color="#0EF0FF", border_color="black", border_width=1.5, hover_color="#6BF6FF", text_color="black")
Button3.place(x=130,y=60)

Button4 = customtkinter.CTkButton(app,command=lambda:show("+"),text="+",font=font1,width=50,height=20,fg_color="#0EF0FF", border_color="black", border_width=1.5, hover_color="#6BF6FF", text_color="black")
Button4.place(x=190,y=60)



Button5 = customtkinter.CTkButton(app,command=lambda:show("7"),text="7",font=font1,width=50,height=20,fg_color="#CDCDCD", border_color="black", border_width=1.5, hover_color="#DEDEDE", text_color="black")
Button5.place(x=10,y=100)

Button6 = customtkinter.CTkButton(app,command=lambda:show("8"),text="8",font=font1,width=50,height=20,fg_color="#CDCDCD", border_color="black", border_width=1.5, hover_color="#DEDEDE", text_color="black")
Button6.place(x=70,y=100)

Button7 = customtkinter.CTkButton(app,command=lambda:show("9"),text="9",font=font1,width=50,height=20,fg_color="#CDCDCD", border_color="black", border_width=1.5, hover_color="#DEDEDE", text_color="black")
Button7.place(x=130,y=100)

Button8 = customtkinter.CTkButton(app,command=lambda:show("-"),text="-",font=font1,width=50,height=20,fg_color="#0EF0FF", border_color="black", border_width=1.5, hover_color="#6BF6FF", text_color="black")
Button8.place(x=190,y=100)



Button9 = customtkinter.CTkButton(app,command=lambda:show("4"),text="4",font=font1,width=50,height=20,fg_color="#CDCDCD", border_color="black", border_width=1.5, hover_color="#DEDEDE", text_color="black")
Button9.place(x=10,y=140)

Button10 = customtkinter.CTkButton(app,command=lambda:show("5"),text="5",font=font1,width=50,height=20,fg_color="#CDCDCD", border_color="black", border_width=1.5, hover_color="#DEDEDE", text_color="black")
Button10.place(x=70,y=140)

Button11 = customtkinter.CTkButton(app,command=lambda:show("6"),text="6",font=font1,width=50,height=20,fg_color="#CDCDCD", border_color="black", border_width=1.5, hover_color="#DEDEDE", text_color="black")
Button11.place(x=130,y=140)

Button12 = customtkinter.CTkButton(app,command=lambda:show("*"),text="x",font=font1,width=50,height=20,fg_color="#0EF0FF", border_color="black", border_width=1.5, hover_color="#6BF6FF", text_color="black")
Button12.place(x=190,y=140)



Button13 = customtkinter.CTkButton(app,command=lambda:show("1"),text="1",font=font1,width=50,height=20,fg_color="#CDCDCD", border_color="black", border_width=1.5, hover_color="#DEDEDE", text_color="black")
Button13.place(x=10,y=180)

Button14 = customtkinter.CTkButton(app,command=lambda:show("2"),text="2",font=font1,width=50,height=20,fg_color="#CDCDCD", border_color="black", border_width=1.5, hover_color="#DEDEDE", text_color="black")
Button14.place(x=70,y=180)

Button15 = customtkinter.CTkButton(app,command=lambda:show("3"),text="3",font=font1,width=50,height=20,fg_color="#CDCDCD", border_color="black", border_width=1.5, hover_color="#DEDEDE", text_color="black")
Button15.place(x=130,y=180)

Button16 = customtkinter.CTkButton(app,command=lambda:show("/"),text="/",font=font1,width=50,height=20,fg_color="#0EF0FF", border_color="black", border_width=1.5, hover_color="#6BF6FF", text_color="black")
Button16.place(x=190,y=180)



Button13 = customtkinter.CTkButton(app,command=lambda:show("."),text=".",font=font1,width=50,height=20,fg_color="#CDCDCD", border_color="black", border_width=1.5, hover_color="#DEDEDE", text_color="black")
Button13.place(x=10,y=220)

Button14 = customtkinter.CTkButton(app,command=lambda:show("0"),text="0",font=font1,width=50,height=20,fg_color="#CDCDCD", border_color="black", border_width=1.5, hover_color="#DEDEDE", text_color="black")
Button14.place(x=70,y=220)

Button15 = customtkinter.CTkButton(app,command=calculate,text="Enter",font=font1,width=110,height=20,fg_color="#0DFF68", border_color="black", border_width=1.5, hover_color="#81FF51", text_color="black")
Button15.place(x=130,y=220)


app.mainloop()