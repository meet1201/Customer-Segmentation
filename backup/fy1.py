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



from mpl_toolkits.mplot3d import Axes3D


#Reading the excel file
# data= pd.read_csv('Mall_Customers.csv')
# data.head()


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
# df1 = data[["CustomerID", "Gender", "Age", "Annual Income (k$)", "Spending Score (1-100)"]]

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

    # Importing KMeans from sklearn


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

    # Taking 5 clusters
    km1 = KMeans(n_clusters=5)
    # Fitting the input data
    km1.fit(X)
    # predicting the labels of the input data
    y = km1.predict(X)
    # adding the labels to a column named label
    df1["label"] = y
    # The new dataframe with the clustering done
    df1.head()

    # Scatterplot of the clusters

    sns.scatterplot(x='Annual Income (k$)', y='Spending Score (1-100)', hue="label",
                    palette=['green', 'orange', 'brown', 'dodgerblue', 'red'], legend='full', data=df1, s=60)
    plt.xlabel('Annual Income (k$)')
    plt.ylabel('Spending Score (1-100)')
    plt.title('Spending Score (1-100) vs Annual Income (k$)')
    plt.show()
   


# 2nd Type Of Clustering with 3 variables
def start2(data):
    df2 = data[["CustomerID", "Gender", "Age", "Annual Income (k$)", "Spending Score (1-100)"]]
    df2.head()
    # Taking the features
    X2 = df2[["Age", "Annual Income (k$)", "Spending Score (1-100)"]]
    # Now we calculate the Within Cluster Sum of Squared Errors (WSS) for different values of k.
    wcss = []
    for k in range(1, 11):
        kmeans = KMeans(n_clusters=k, init="k-means++")
        kmeans.fit(X2)
        wcss.append(kmeans.inertia_)


    plt.plot(range(1, 11), wcss, linewidth=2, color="red", marker="8")
    plt.xlabel("K Value")
    plt.xticks(np.arange(1, 11, 1))
    plt.ylabel("WCSS")
    plt.show()

    # We choose the k for which WSS starts to diminish
    km2 = KMeans(n_clusters=5)
    y2 = km2.fit_predict(X2)
    df2["label"] = y2
    # The data with labels
    df2.head()

    # 3D Plot as we did the clustering on the basis of 3 input features
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(df2.Age[df2.label == 0], df2["Annual Income (k$)"][df2.label == 0],
               df2["Spending Score (1-100)"][df2.label == 0], c='purple', s=60)
    ax.scatter(df2.Age[df2.label == 1], df2["Annual Income (k$)"][df2.label == 1],
               df2["Spending Score (1-100)"][df2.label == 1], c='red', s=60)
    ax.scatter(df2.Age[df2.label == 2], df2["Annual Income (k$)"][df2.label == 2],
               df2["Spending Score (1-100)"][df2.label == 2], c='blue', s=60)
    ax.scatter(df2.Age[df2.label == 3], df2["Annual Income (k$)"][df2.label == 3],
               df2["Spending Score (1-100)"][df2.label == 3], c='green', s=60)
    ax.scatter(df2.Age[df2.label == 4], df2["Annual Income (k$)"][df2.label == 4],
               df2["Spending Score (1-100)"][df2.label == 4], c='yellow', s=60)
    ax.view_init(35, 185)
    plt.xlabel("Age")
    plt.ylabel("Annual Income (k$)")
    ax.set_zlabel('Spending Score (1-100)')
    plt.show()
    return df2
    
status = False

def show_graphs(*args):

    annual_income(data)
    age(data)
    spending_score(data)
    genders(data)
    age_vs_ai(data)
    age_vs_nc(data)

# show_graphs(data)
# start(data)
# start2(data)

# def read_file():
    
#     csv_file_path = askopenfilename()
#     if len(csv_file_path) > 1:
#         status = True
#         tkinter.messagebox.showinfo("Info", "Your File Successfully selected")
#         print(csv_file_path)
#         data = pd.read_csv(csv_file_path)
#         return data.head()
        

        

# def startProgram(data):
#     tkinter.messagebox.showinfo("Info", "Please wait a while, Processing your Database...")
# #     start(data)

# def show_graphs():

#     annual_income(data)
#     age(data)
#     spending_score(data)
#     genders(data)
#     age_vs_ai(data)
#     age_vs_nc(data)








root = Tk()
# root.withdraw() #Prevents the Tkinter window to come up
exlpath = askopenfilename()
# root.destroy()
print(exlpath)
data= pd.read_csv(exlpath)
print(data)

p1 = PhotoImage(file = '/Users/meetpatel/Desktop/Meet Documents/FinalYear/logo.png')
# Icon set for program window
root.iconphoto(True, p1)

root.title('Customer Segmentation Program')
root.minsize(710, 550)
root.maxsize(710, 550)
root.configure(background="skyblue4")




heading = Label(root, text="Welcome to Customer Segmentation System", fg='black', bg="lemon chiffon")
heading.configure(font=("Calibri", 35))
heading.pack(fill="x")

# img = ImageTk.PhotoImage(Image.open('/Users/meetpatel/Desktop/Meet Documents/FinalYear/logo2.png'))
# labelImage = Label(root, image=img, borderwidth=0, width=150, height=150)
# labelImage.pack(pady=(2,0))


def open_text():
    pass
# my_text= Text(root,width=40, height=10, font=("Helvetica",16))
# my_text.pack(pady=20)

# btn1 = Button(root, text="Add CSV File", fg="black", bg="#80182A", width=25, height=2, command=read_file,font=('Arial',16,'bold')).pack(pady=(20, 20))
btn2 = Button(root, text="Show Graphs", fg="black", bg="#80182A", width=25, height=4, command=show_graphs, font=('Arial',16,'bold'),activeforeground="red").pack(pady=(100,20))
btn3 = Button(root, text="Start Program", fg="black", bg="#80182A", width=25, height=4, command=start,font=('Arial',16,'bold'),activeforeground="red").pack(pady=(20, 20))
btn4 = Button(root, text="Customer Division", fg="black", bg="#80182A", width=25, height=4, command=open_text,font=('Arial',16,'bold'),activeforeground="red").pack(pady=(20, 20))

root.mainloop()

# Cluster1 shows the customers with average salary and average spending so we can categorize these customers as
# Cluster2 shows the customer has a high income but low spending, so we can categorize them as careful.
# Cluster3 shows the low income and also low spending so they can be categorized as sensible.
# Cluster4 shows the customers with low income with very high spending so they can be categorized as careless.
# Cluster5 shows the customers with high income and high spending so they can be categorized as target, and these customers can be the most profitable customers for the mall owner.
