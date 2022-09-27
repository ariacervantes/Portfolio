# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 08:32:05 2022

@author: Ariathna
"""

import pandas as pd
data= pd.read_csv('transaction.csv', sep= ';')

#Summary of the data

data.info()

#Calculations

CostPerItem= data['CostPerItem']
NumberOfItemsPurchased= data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem * NumberOfItemsPurchased

#addind new column

data['CostPerTransaction']= CostPerTransaction

#sales per transaction

data['SalesPerTransaction']= data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

#Profit Calculation = Sale - Cost

data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

#Markup = (Sale - Cost)/ Cost

data['Markup']=data['ProfitPerTransaction'] / data['CostPerTransaction']

#Roundind

RoundMarkup = round(data['Markup'],2)

data['Markup'] = round(data['Markup'],2)

#Combining Data Fields
#First we need our variables to be string

day = data['Day'].astype(str)
year = data['Year'].astype(str)

Date = day+'-'+data['Month']+'-'+year
data['Date']=Date

data.head(10)
data.iloc[:,2]

#Split the column ClientKeyWords

split_col = data['ClientKeywords'].str.split(',', expand=True)

#Naming the columns

data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['ClientContract'] = split_col[2]

#Using replace to delete brakets

data['ClientAge'] = data['ClientAge'].str.replace('[','')
data['ClientContract'] = data['ClientContract'].str.replace(']','')

#Changing description to low case

data['ItemDescription']=data['ItemDescription'].str.lower()

#Merging Files

seasons= pd.read_csv('value_inc_seasons.csv', sep= ';')

data= pd.merge(data, seasons, on='Month')

#Dropping Columns

data= data.drop(['ClientKeywords','Day','Month','Year'], axis=1)
#data= data.drop('Day', axis=1)
#data= data.drop('Month', axis=1)
#data= data.drop('Year', axis=1)

#EXPORTING DATA TO CSV

data.to_csv('ValueINC_Clean.csv', index=False)