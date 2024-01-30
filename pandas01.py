# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 04:31:27 2024

@author: Aoate Tsimatsima
"""

import pandas

file = pandas.read_csv("country_data.csv")

print(file)
***
#Age Gender       Country
0    39      M  South Africa
1    25      M      Botswana
2    29      F  South Africa
3    46      M  South Africa
4    22      F         Kenya
5    35      F    Mozambique
6    22      F       Lesotho
7    49      M         Kenya
8    30      M         Kenya
9    40      F         Egypt
10   30      M         Sudan
#hlpsake sure that all the columns have the right format of data
print(file.info())  
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 11 entries, 0 to 10
Data columns (total 3 columns):
 #   Column   Non-Null Count  Dtype 
---  ------   --------------  ----- 
 0   Age      11 non-null     int64 
 1   Gender   11 non-null     object
 2   Country  11 non-null     object
dtypes: int64(1), object(2)
memory usage: 396.0+ bytes
None

print(file.describe())
             Age
count  11.000000
mean   33.363636
std     9.233339
min    22.000000
25%    27.000000
50%    30.000000
75%    39.500000
max    49.000000
#Practice session
iris = pandas.read_csv("iris.csv")
print(iris)
print(iris.info())
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 150 entries, 0 to 149
Data columns (total 5 columns):
 #   Column        Non-Null Count  Dtype  
---  ------        --------------  -----  
 0   sepal_length  150 non-null    float64
 1   sepal_width   150 non-null    float64
 2   petal_length  150 non-null    float64
 3   petal_width   150 non-null    float64
 4   species       150 non-null    object 
dtypes: float64(4), object(1)
memory usage: 6.0+ KB
None

print(iris.describe())
      sepal_length  sepal_width  petal_length  petal_width
count    150.000000   150.000000    150.000000   150.000000
mean       5.843333     3.054000      3.758667     1.198667
std        0.828066     0.433594      1.764420     0.763161
min        4.300000     2.000000      1.000000     0.100000
25%        5.100000     2.800000      1.600000     0.300000
50%        5.800000     3.000000      4.350000     1.300000
75%        6.400000     3.300000      5.100000     1.800000
max        7.900000     4.400000      6.900000     2.500000


diab_data = pandas.read_csv("diab_data.csv")
print(diab_data)
print(diab_data.info())
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 768 entries, 0 to 767
Data columns (total 9 columns):
 #   Column      Non-Null Count  Dtype  
---  ------      --------------  -----  
 0   preg_count  768 non-null    int64  
 1   glucose     768 non-null    int64  
 2   bp          768 non-null    int64  
 3   skinfold    768 non-null    int64  
 4   insulin     768 non-null    int64  
 5   BMI         768 non-null    float64
 6   predigree   768 non-null    float64
 7   age         768 non-null    int64  
 8   class       768 non-null    int64  
dtypes: float64(2), int64(7)
memory usage: 54.1 KB
None

print(diab_data.describe())
      preg_count     glucose          bp  ...   predigree         age       class
count  768.000000  768.000000  768.000000  ...  768.000000  768.000000  768.000000
mean     3.845052  120.894531   69.105469  ...    0.471876   33.240885    0.348958
std      3.369578   31.972618   19.355807  ...    0.331329   11.760232    0.476951
min      0.000000    0.000000    0.000000  ...    0.078000   21.000000    0.000000
25%      1.000000   99.000000   62.000000  ...    0.243750   24.000000    0.000000
50%      3.000000  117.000000   72.000000  ...    0.372500   29.000000    0.000000
75%      6.000000  140.250000   80.000000  ...    0.626250   41.000000    1.000000
max     17.000000  199.000000  122.000000  ...    2.420000   81.000000    1.000000

[8 rows x 9 columns]
column_names = ["A", "B", "C", "D","E","F","G","H","I","J","K","L","M","N"]
housing_data = pandas.read_csv("housing_data.csv",column_names)
print(housing_data) #no names for each of the columns

print(housing_data.info())
print(housing_data.describe())

#insurance data was edited in exel to remove text not needed
insurance_data = pandas.read_csv("insurance_data.csv")
print(insurance_data)
print(insurance_data.info())
print(insurance_data.describe())
#use skiprows funtion
insurance_data_2 = pandas.read_csv("insurance.csv",skiprows= 5

#When importing data and there are spaces or unwanted characters,use sep = ""
#datasets with sapces may give an error
#storing data
B1 = 30
B2 = 40
B3 = 30
B4 = 49
print(B2)


#USING LISTS [] indexes- always start at 0
age = [39,25,29,46,22,35,22,49,30,40,30]
print(age) #the defined list will appear
#the index always starts at 0 - so the fisrt element will be 0, sencond 1, and so on

print(age[10]) # will display the 11th element
 
#basic stats
print(min(age))
print(max(age))
print(len(age))
print(sum(age))
# no mean/ average function hence one needs to make an equation

average = sum(age)/len(age)
print(average)
#listrs are a better option compared to adding the individual variables. they can be accesed the same way 


#gender list

gender = ["M","M","F","M","F","F","F","M","M","F","M"]

print(gender[2])
print(gender[-1]) #last value in the list


country = ["South Africa","Botswana","South Africa","South Africa","Kenya","Mozambique","Lesotho","Kenya","Kenya","Egypt","Sudan"]
print(country)
print(country[5])


#datastorage with lists

my_list = [42,-2021,6.283,"tau","node"]

print(my_list)
print(my_list[:])

my_list.append("pi")
print(my_list)


my_list.insert(1,"pi2")
print(my_list)

my_list.remove("pi")
my_list.remove("pi2")
my_list.remove("tau")
print(my_list)
print(my_list[0:3])#look at range
#ertain range of values from a list we call this list slicing


#Dictionary {}collection of key-value pairs, where each key is unique
#keys are like column names and values are the list of data

#syntax d = {'key1': 'value1', 'key2': 'value2'} key and value pairs

person = {'name': 'Oteng Tsimatsima', 'age': 29,'address': '123 Main St.'}
print(person['name'])
person['phone'] = '000000000' #to add another column

cars = {'toyota': "yaris", 'renault': "megane", 'suzuki': "swift"}
print(cars['renault'])
#DATA frame

import pandas as pd #pd is a shortcut of using pandas
data = {'age': [39,25,29,46,22,35,22,49,30,40,30], 'gender': ["M","M","F","M","F","F","F","M","M","F","M"],'country':["South Africa","Botswana","South Africa","South Africa","Kenya","Mozambique","Lesotho","Kenya","Kenya","Egypt","Sudan"]}
patients = {'names' : ["Mpumi","Lesedi","Sandy","Pinky","Chicken"],'likes':["candy","fruit","vegetables","water","beef"], 'number_of_children': [3,9,2,0,3], 'age': [56,56,78,34,76]}
patients_df = pd.DataFrame(patients)

df = pd.DataFrame(data) #df -will be dataframe
print(patients_df)
print(df) #display dataframe
#the dataframe now contains whole dataset with its columns
#    age gender       country
#0    39      M  South Africa
#1    25      M      Botswana
#2    29      F  South Africa
#3    46      M  South Africa
#4    22      F         Kenya
#5    35      F    Mozambique
#6    22      F       Lesotho
#7    49      M         Kenya
#8    30      M         Kenya
#9    40      F         Egypt
#10   30      M         Sudan

#accesing specific columns

print(df['age'])

#basic stats
print(df['age'].max())

#filtering data
print(df[df['age'] > 30])#bigger than 30

#slicing rows and columns
print(df[1:4]) #row 1 to 4 were selected will all the columns 

#adding ne columns
df['new_column'] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(df)
#removing
df.drop(columns=['new_column'], inplace=True)# add true because its boolean parameter that are recongnised to??? google
print(df)
####################################################################

knownblusterblast = pandas.read_table("knownclusterblastoutput.txt")
print(knownblusterblast)
print(knownblusterblast.info())

















