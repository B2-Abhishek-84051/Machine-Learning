# i) Create a list of empids and names (10 employees).
#    ii) Convert list into Series.
#    iii) Print type of Series.
#    iv) Convert Series into DataFrame.
#    v) a) Display all records.
#       b) Display first five records.
#       c) Display last five records.
#    vi) Save the record in csv file (MyRecord.csv)
import pandas as pd

empid = [101,102,103,104,105,106,107,108,109,110]
name = ["Employee1", "Employee2", "Employee3", "Employee4", "Employee5", "Employee6", "Employee7", "Employee8", "Employee9", "Employee10"]

emp_series = pd.Series(name, index=empid)
print(emp_series)

print('-'*50)
print(f"Type of empid = {type(empid)}, type of name = {type(name)}")
print("type of emp_series = "+str(type(emp_series)))
print('-'*50)

df = pd.DataFrame(emp_series)
print(df)
print('-' * 50)
print(df.head(5))
print('-' * 50)
print(df.tail(5))
print('-' * 50)

with open('./MyRecord.csv', 'w') as file:
    df.to_csv(file)
print("file written successfully")