#  write your code here 
import pandas as pd


if __name__ == "__main__":
    df = pd.read_csv("/Users/aragonerua/PycharmProjects/Data Analysis for Hospitals/Topics/Handling missing values/Replace with the mode/data/dataset/input.txt", sep=",")
    modes = df["location"].mode()[0]
    df["location"].fillna(modes, inplace=True)
    print(df.head(5))
