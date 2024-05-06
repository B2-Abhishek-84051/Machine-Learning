# 1. Consider each of following datasets and do below operations.
# i) Read the dataset.
# ii) Display first 5 and last 5 records.
# iii) Display info and describe the dataset.
# iv) Find out null values.
# v) Plot Various graphs. e.g. barchart, scatterplot, histogram, lineplot, pairplot
#
# Datasets:
#
# i) ToyotaCorolla.csv
# ii) Engine.csv
# iii) delivery_time.csv
# iv) SAT-GPA.csv
# v) TvMarketing.csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def function1():
    df = pd.read_csv('./ToyotaCorolla.csv', encoding='latin1')
    print('-'*50)
    print(df.head(5))
    print(df.tail(5))
    print('-'*50)
    print(df.info)
    print('-'*50)
    print(df.describe())
    print('-'*50)
    print(df.isna().sum())

    plt.xlabel("ID")
    plt.ylabel("Price")
    plt.title("Price Pattern")

    x = np.arange(df['Id'].size)
    plt.plot(x, df['Price'], color="green", label="Price Graph")
    plt.show()

# function1()

def function2():
    df = pd.read_csv('./Engine.csv')
    print(df.head(5))
    print(df.tail(5))
    print('-'*50)
    print(df.info)
    print('-'*50)
    print(df.describe())
    print('-'*50)
    print(df.isna().sum())

    plt.xlabel("Engine Size")
    plt.ylabel("Cylinder")

    x = np.arange(df["ENGINESIZE"].size)
    plt.bar(df["ENGINESIZE"], df["CYLINDERS"], label="Engine Size")
    # plt.hist(df["ENGINESIZE"])
    plt.title("Engine Size Vs Cylinder")
    plt.legend()
    plt.show()

# function2()

def function3():
    df = pd.read_csv('./delivery_time.csv')
    print(df.head(5))
    print(df.tail(5))
    print('-'*50)
    print(df.info())
    print('-'*50)
    print(df.describe())
    print('-'*50)
    print(df.isna().sum())

    plt.xlabel("Delivery Time")
    plt.ylabel("Sorting Time")
    plt.title("Delivery time vs Sorting time")

    plt.scatter(df["Delivery Time"], df["Sorting Time"], label="Delivery time vs Sorting time")

    plt.legend()
    plt.show()

# function3()

def function4():
    df = pd.read_csv('./SAT-GPA.csv')
    print(df.head(5))
    print(df.tail(5))
    print('-'*50)
    print(df.info())
    print('-'*50)
    print(df.describe())
    print('-'*50)
    print(df.isna().sum())
    print('-' * 50)

    plt.plot(df['SAT'], df['GPA'], color="orange", label="SAT vs GPA")

    plt.xlabel("SAT")
    plt.ylabel("GPA")
    plt.title("GPA vs SAT")
    plt.legend()
    plt.show()

# function4()

def function5():
    df = pd.read_csv('./TvMarketing.csv')
    print(df.head(5))
    print(df.tail(5))
    print('-'*50)
    print(df.info())
    print('-' * 50)
    print(df.describe())
    print('-' * 50)
    print(df.isna().sum())
    print('-'*50)

    plt.hist(df['TV'], color="orange", label="TV")
    plt.hist(df['Sales'], color="green", label="Sales")

    plt.xlabel("TV")
    plt.ylabel("Sales")
    plt.title("TV vs Sales")
    plt.legend()
    plt.show()

function5()