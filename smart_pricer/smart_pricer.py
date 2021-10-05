''' Smart Pricer Data Analyst Role Challenge'''
#Given data_export.csv
#imports
import pandas as pd
import os
# 1. read as pandas dataframe. separator = ; , decimal = ,
df = pd.read_csv("./data_export.csv", sep =';', encoding = 'unicode_escape', decimal=",")
# drop columns 'Land' and 'purchase_dt'; convert 'event_date' to Date and sort
df['event_date'] =pd.to_datetime(df.event_date)
df_new = df.drop('land',axis=1)
df_new = df_new.drop('purchase_dt',axis=1)
df_new.sort_values(by='event_date')
#iterate over left over columns;
# Make new Dataframe(columns= unique values,no. of tickets, total revenue grouped by unique values)
# and write to csv
for column in df_new.columns:
    uni = df_new[column].unique()
    #print(f"There are {len(uni)} Unique Values in {column}. They are : {uni}")
    column_df = df_new.groupby([column]).size().reset_index(name='No. of Tickets')
    print(column_df.head())

    column_df['Total Revenue'] = df_new.groupby([column])[['price']].aggregate('sum').rename(columns={"price": "Total Revenue"}).reset_index()['Total Revenue']
    column_df.to_csv(f'./output/{column}.csv', sep =';', decimal=",")
os.rename('./output/event_date.csv','./output/fingerprint.csv')
