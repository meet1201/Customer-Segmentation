from tkinter import *
import tkinter.messagebox
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
import pandas as pd
from fy import *



data = pd.read_csv('Mall_Customers.csv')
# def read_file():
    
#     csv_file_path = askopenfilename()
#     if len(csv_file_path) > 1:
#         tkinter.messagebox.showinfo("Info", "Your File Successfully selected")
#         print(csv_file_path)
#         data = pd.read_csv(csv_file_path)
#         return data.head()

        

def startProgram(data):
    tkinter.messagebox.showinfo("Info", "Please wait a while, Processing your Database...")
#     start(data)

def show_graphs():
    
    annual_income(data)
    age(data)
    spending_score(data)
    genders(data)
    age_vs_ai(data)
    age_vs_nc(data)






def output():

    T = Text(root, height = 5, width = 52)
    T.insert('end',customer_division(pl))

root = Tk()
root.title('Customer Segmentation Program')
root.minsize(910, 695)
root.maxsize(910, 695)
root.configure(background="black")


heading = Label(root, text="Welcome to Customer Segmentation System", fg='#CDCDCD', bg="#80182A")
heading.configure(font=("Arial", 35))
heading.pack(fill="x")

# btn1 = Button(root, text="Add CSV File", fg="#CDCDCD", bg="#80182A", width=25, height=2, command=read_file).pack(pady=(5, 20))
btn2 = Button(root, text="Show Graphs", fg="#CDCDCD", bg="#80182A", width=25, height=2, command=show_graphs).pack(pady=(0, 20))
btn3 = Button(root, text="Start Program", fg="#CDCDCD", bg="#80182A", width=25, height=2, command=startProgram).pack(pady=(0, 20))
btn4 = Button(root, text="Customer Division", fg="#CDCDCD", bg="#80182A", width=25, height=2, command=output).pack(pady=(0, 20))

root.mainloop()