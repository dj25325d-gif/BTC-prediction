import matplotlib.pyplot as plt
import seaborn as sns

def linechart(df, xcol, ycol):
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(data=df, x=xcol, y=ycol, color="green")
    plt.title(ycol + " by " + xcol)
    plt.xlabel(xcol)
    plt.ylabel(ycol)
    plt.xticks(rotation=45)

def barchart(df, xcol, ycol):
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(data=df, x=xcol, y=ycol, color="blue")
    plt.title(ycol + " grouped by " + xcol)
    plt.xlabel(xcol)
    plt.ylabel(ycol)
    plt.xticks(rotation=45)

def scatterplot(df, xcol, ycol):
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.scatterplot(data=df, x=xcol, y=ycol, alpha=0.6, color="orange")
    plt.title(xcol + " vs " + ycol)
    plt.xlabel(xcol)
    plt.ylabel(ycol)

def dohistogram(df, col):
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.histplot(df[col], kde=True, color="purple", bins=50)
    plt.title("Distribution of " + col)
    plt.xlabel(col)
    plt.ylabel("Frequency")

def piechart(df, col):
    fig, ax = plt.subplots(figsize=(12, 6))
    df[col].value_counts().plot.pie(autopct='%0.2f%%', colors=sns.color_palette("pastel"))
    plt.title("Breakdown of " + col)
    plt.ylabel("")  

def areachart(df, cols):
    fig, ax = plt.subplots(figsize=(12, 6))
    df[cols].plot.area(alpha=0.4, ax=ax)
    plt.title("Area Plot")
    plt.xlabel("Index")
    plt.ylabel("Values")
