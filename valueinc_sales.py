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
data.iloc[0]