import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
df= pd.read_excel("C:/Users/ADMIN/Desktop/car_purchasing.xlsx")
df

country=df["country"]
list_country=list(country)
list_country
 


net_worth=df["net worth"]
list_worth=list(net_worth)
list_worth

country_worth=list(zip(list_country,list_worth))
country_worth

########we want to find the networth of each conrty
Q={}
for a,b in country_worth:
    if a not in Q:
        Q[a]={}
        ####iterete over each networth in every city
        if b in Q[a]:
            Q[a][b] +=1
        else:
            Q[a][b] =1
            print(Q)
J=list(Q.keys())
K=list(Q.values())
list_dict=list(zip(J,K))
list_dict
df_dict=pd.DataFrame(list_dict) 
df_dict   
    
df_dict.describe()  
df_dict.corr()
#####Subset the original dataframe
###to get the contry and networth then comapre the two dataframes
Df2=df[['country','net worth']]
Df2
 



