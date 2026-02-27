import pandas as pd

data = {
    "id" : [1,2,3,4,5,6,7,8,9,2],
    "Name" : ["Niket","Amit","Rutuja","Jigar","Charul","Het","Krish","vishakha","Bot","Amit"],
    "Phone Number" : [9879876543,5676543212,4567876543,5678900987,7890656789,8900987654,6789876543,5678900987,7890656789,5676543212],
    "DOB" : ["03-02-2005","01-12-2004","04-02-2004","23-05-2004","12-11-2003","24-05-2003","22-08-2005","12-03-2002","01-01-2001","01-12-2004"],
    "Age" : [21,22,22,22,23,230,21,24,25,22],
    "Gendar" : ["Male","Male","Female","Male","Female","Male","Male","Female","Female","Male"],
    "Roll Number" : [103,99,41,78,201,205,56,72,93,99],
    "Science Marks" : [88,50,76,None,90,56,40,76,87,50],
    "Computer Marks" : [76,65,50,57,74,87,None,65,56,65],
    "Maths Marks" : [90,67,75,65,None,76,40,56,76,67],
    "SS Marks" : [56,70,40,50,60,65,45,78,86,70],
    "Total Marks" : [310,252,241,237,304,284,170,275,305,252],
    "Percentage" : [77.5,63.0,60.25,59.25,76.0,71.0,42.5,68.75,76.25,63.0],
    "Grade" : ["B","C","C","D","B","B","D","C","B","C"],
    "Result" : ["Pass","Pass","Pass","Pass","Pass","Pass","Fail","Pass","Pass","Pass"]
}

df = pd.DataFrame(data)
print(df.to_string())
print(df.isnull())
print(df.duplicated())
df.drop_duplicates(inplace=True)
a = df["Age"].median().round(0).astype(int)
for i in df.index:
    if df.loc[i,"Age"] > 80:
        df.loc[i,"Age"] = a
b = df["Science Marks"].mean().round(0).astype(int)
df.fillna({"Science Marks":b}, inplace=True)
c = df["Computer Marks"].median().round(0).astype(int)
df.fillna({"Computer Marks":c}, inplace=True)
d = df["Maths Marks"].mode()
df.fillna({"Maths Marks":d}, inplace=True)
print(df.head(2))
print(df.tail(2))
print(df.shape)
print(df.describe())
print(df.to_string())