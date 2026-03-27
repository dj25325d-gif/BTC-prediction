def toprow(df, num=5):
    print(df.head(num))

def botrow(df, num=5):
    print(df.tail(num))

def colnames(df):
    print("Here are the columns:")
    print(df.columns)

def datatypes(df):
    print("Data types:")
    print(df.dtypes)

def randomrows(df, num=5):
    print(df.sample(num))
