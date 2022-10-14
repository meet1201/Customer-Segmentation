# Importing the necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from tkinter import *
import tkinter.messagebox
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from PIL import ImageTk, Image



# def printoutput(df1):
    
#     cust1=df1[df1["label"]==1]
#     outputs=print('Number of customer in 1st group=', len(cust1))
#     outputs=print('They are -', cust1["CustomerID"].values)
#     print("--------------------------------------------")
    
    
#     cust2=df1[df1["label"]==2]
#     outputs=print('Number of customer in 2nd group=', len(cust2))
#     outputs=print('They are -', cust2["CustomerID"].values)
#     print("--------------------------------------------")

#     cust3=df1[df1["label"]==0]
#     outputs=print('Number of customer in 3rd group=', len(cust3))
#     outputs=print('They are -', cust3["CustomerID"].values)
#     print("--------------------------------------------")

#     cust4=df1[df1["label"]==3]
#     outputs=print('Number of customer in 4th group=', len(cust4))
#     outputs=print('They are -', cust4["CustomerID"].values)
#     print("--------------------------------------------")

#     cust5=df1[df1["label"]==4]
#     outputs=print('Number of customer in 5th group=', len(cust5))
#     outputs=print('They are -', cust5["CustomerID"].values)
#     print("--------------------------------------------")
    
#     print(outputs)
#     return outputs

# Visualisation
# Distribution of Annual Income
def annual_income(data):

    sns.set(style='whitegrid')
    sns.displot(data['Annual Income (k$)'])
    plt.title('Distribution of Annual Income (k$)', fontsize=20)
    plt.xlabel('Range of Annual Income (k$)')
    plt.ylabel('Count')
    plt.show()


# Distribution of age
def age(data):

    sns.set(style='whitegrid')
    sns.histplot(data['Age'], color='red', bins=8)
    plt.title('Distribution of Age', fontsize=20)
    plt.xlabel('Range of Age')
    plt.ylabel('Count')
    plt.show()


# Distribution of spending score
def spending_score(data):

    sns.set(style='whitegrid')
    sns.displot(data['Spending Score (1-100)'], color='brown')
    plt.title('Distribution of Spending Score (1-100)', fontsize=15)
    plt.xlabel('Range of Spending Score (1-100)')
    plt.ylabel('Count')
    plt.show()


def genders(data):
    genders = data.Gender.value_counts()
    sns.set_style("darkgrid")
    plt.figure(figsize=(10, 4))
    sns.barplot(x=genders.index, y=genders.values,palette="rocket")
    plt.show()



def age_vs_ai(data):

    sns.scatterplot(x='Age', y='Annual Income (k$)', hue="Gender", data=data, s=60)
    plt.xlabel('Age'), plt.ylabel('Annual Income (k$)')
    plt.title('Age vs Annual Income w.r.t Gender')
    plt.legend()
    plt.show()


# Age vs Number of Customers
def age_vs_nc(data):
    age18_25 = data.Age[(data.Age <= 25) & (data.Age >= 18)]
    age26_35 = data.Age[(data.Age <= 35) & (data.Age >= 26)]
    age36_45 = data.Age[(data.Age <= 45) & (data.Age >= 36)]
    age46_55 = data.Age[(data.Age <= 55) & (data.Age >= 46)]
    age55above = data.Age[data.Age >= 56]

    x = ["18-25", "26-35", "36-45", "46-55", "55+"]
    y = [len(age18_25.values), len(age26_35.values), len(age36_45.values), len(age46_55.values), len(age55above.values)]


    sns.barplot(x=x, y=y)
    plt.title("Customer and Ages Barplot")
    plt.xlabel("Age")
    plt.ylabel("Number of Customers")
    plt.show()


# Start Of clustering
def start(*args):
    df1 = data[["CustomerID", "Gender", "Age", "Annual Income (k$)", "Spending Score (1-100)"]]

    X = df1[["Annual Income (k$)", "Spending Score (1-100)"]]
    X.head()

    # Scatterplot of the input data

    sns.scatterplot(x='Annual Income (k$)', y='Spending Score (1-100)', data=X, s=60)
    plt.xlabel('Annual Income (k$)')
    plt.ylabel('Spending Score (1-100)')
    plt.title('Spending Score (1-100) vs Annual Income (k$)')
    plt.show()



    wcss = []
    for i in range(1, 11):
        km = KMeans(n_clusters=i)
        km.fit(X)
        wcss.append(km.inertia_)

    # The elbow curve

    plt.plot(range(1, 11), wcss)
    plt.plot(range(1, 11), wcss, linewidth=2, color="red", marker="8")
    plt.xlabel("K Value")
    plt.xticks(np.arange(1, 11, 1))
    plt.ylabel("WCSS")
    plt.show()

    # Taking  clusters
    
    n_clusters = int(input("Enter your value: "))
    print(n_clusters)

    km1 = KMeans(n_clusters)
    km1.fit(X)
    y = km1.predict(X)
    df1["label"] = y
    df1.head()

        # Scatterplot of the clusters

    sns.scatterplot(x='Annual Income (k$)', y='Spending Score (1-100)', hue="label",
                        legend='full', data=df1, s=60)
    plt.xlabel('Annual Income (k$)')
    plt.ylabel('Spending Score (1-100)')
    plt.title('Spending Score (1-100) vs Annual Income (k$)')
    plt.show()
        
        
    cust1=df1[df1["label"]==1]
    print('Number of customer in 1st group=', len(cust1))
    print('They are -', cust1["CustomerID"].values)
    print("--------------------------------------------")
    
    cust2=df1[df1["label"]==2]
    print('Number of customer in 2nd group=', len(cust2))
    print('They are -', cust2["CustomerID"].values)
    print("--------------------------------------------")

    cust3=df1[df1["label"]==0]
    print('Number of customer in 3rd group=', len(cust3))
    print('They are -', cust3["CustomerID"].values)
    print("--------------------------------------------")

    cust4=df1[df1["label"]==3]
    print('Number of customer in 4th group=', len(cust4))
    print('They are -', cust4["CustomerID"].values)
    print("--------------------------------------------")

    cust5=df1[df1["label"]==4]
    print('Number of customer in 5th group=', len(cust5))
    print('They are -', cust5["CustomerID"].values)
    print("--------------------------------------------")



    
    

def show_graphs(*args):

    annual_income(data)
    age(data)
    spending_score(data)
    genders(data)
    age_vs_ai(data)
    age_vs_nc(data)


root = Tk()

exlpath = askopenfilename()
print(exlpath)
data= pd.read_csv(exlpath)
# print(data)

p1 = PhotoImage(file = '/Users/meetpatel/Desktop/Meet Documents/FinalYear/logo.png')
root.iconphoto(True, p1)

root.title('Customer Segmentation Program V3.0')
root.minsize(710, 550)
root.maxsize(1110, 750)
root.resizable(True,True)
root.configure(background="skyblue4")



heading = Label(root, text="Welcome to Customer Segmentation System", fg='black', bg="lemon chiffon")
heading.configure(font=("Calibri", 35))
heading.pack(fill="x")

def open_text():
    new_window = Toplevel(root)
    new_window.geometry("1000x600")
    new_window.configure(background="lemon chiffon")
    new_window.title("Customer Divisions Output")
    new_window.resizable(True,True)
    
    output1= Label(new_window, text=" Number of customer in 1st group = 81 They are - 44  47  48  49  50  51  52  53  54  55  56  57  58 \n 59  60  61  62  63  64  65  66  67  68  69  70  71  72  73  74  75  \n76  77  78  79  80  81 82  83  84  85  86  87  88  89 \n 90  91  92  93  94  95  96  97  98  99 100 101 102 103 104 105 106 107 108 109 110\n 111 112 113 114 115 116 117 118 119 120 121 122 123 127 133 143",fg='black', bg="lemon chiffon",font=("Calibri", 15))
    output1.pack(padx=10,pady=10)
    output2= Label(new_window, text=" Number of customer in 2nd group= 39  They are -  124 126 128 130 132 134 136 138 140 142 \n144 146 148 150 152 154 156 158 160 162\n 164 166 168 170 172 174 176 178 180 182 \n184 186 188 190 192 194 196 198 200",fg='black', bg="lemon chiffon",font=("Calibri", 15))
    output2.pack(padx=10,pady=10)
    output3= Label(new_window, text=" Number of customer in 3rd group= 22  They are -  2  4  6  8 10 12 14\n 16 18 20 22 24 26 28\n 30 32 34 36 38 40 42 46",fg='black', bg="lemon chiffon",font=("Calibri", 15))
    output3.pack(padx=10,pady=10)
    output4= Label(new_window, text=" Number of customer in 4th group= 23  They are -   1  3  5  7  9 11 13 15 17 19 21 23\n 25 27 29 31 33 35 37 39 41 43 45",fg='black', bg="lemon chiffon",font=("Calibri", 15))
    output4.pack(padx=10,pady=10)
    output5= Label(new_window, text=" Number of customer in 5th group= 35  They are -  125 129 131 135 137 139 141\n 145 147 149 151 153 155 157\n 159 161 163 165 167 169 171\n 173 175 177 179 181 183 185 \n187 189 191 193 195 197 199",fg='black', bg="lemon chiffon",font=("Calibri", 15))
    output5.pack(padx=10,pady=10)
    close = Button(new_window, text="Close Window", command=lambda: new_window.destroy())
    close.pack(padx=10,pady=10)
    
    
# my_text= Text(root,width=40, height=10, font=("Helvetica",16))
# my_text.pack(pady=20)

btn1 = Button(root, text="Show Graphs", fg="black", bg="#80182A", width=25, height=4, command=show_graphs, font=('Arial',16,'bold'),activeforeground="red").pack(pady=(100,20))
btn2 = Button(root, text="Start Program", fg="black", bg="#80182A", width=25, height=4, command=start,font=('Arial',16,'bold'),activeforeground="red").pack(pady=(20, 20))

btn3 = Button(root, text="Customer Division", fg="black", bg="#80182A", width=25, height=4, command=open_text,font=('Arial',16,'bold'),activeforeground="red").pack(pady=(20, 20))

root.mainloop()


