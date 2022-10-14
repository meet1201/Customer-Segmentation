def printoutput(df1):
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

    def customer_division(*args):
        cust1 = df1[df1["label"] == 1]
        print('1st group - average salary and average spending', len(cust1))
        print('They are: ', cust1["CustomerID"].values)
        print("--------------------------------------------")

        cust2 = df1[df1["label"] == 2]
        print('2nd group - high income but low spending', len(cust2))
        print('They are: ', cust2["CustomerID"].values)
        print("--------------------------------------------")

        cust3 = df1[df1["label"] == 0]
        print('3rd group - low income and also low spending ', len(cust3))
        print('They are: ', cust3["CustomerID"].values)
        print("--------------------------------------------")

        cust4 = df1[df1["label"] == 3]
        print('4th group - low income with very high spending ', len(cust4))
        print('They are: ', cust4["CustomerID"].values)
        print("--------------------------------------------")

        cust5 = df1[df1["label"] == 4]
        print('5th group - high income and high spending ', len(cust5))
        print('They are: ', cust5["CustomerID"].values)
        print("--------------------------------------------")
        print("////////////////////////////////////////////")
