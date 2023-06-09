import pandas as pd
df=pd.read_csv("Data_set.csv")
print(df)
df.head (10)
df.info()
df.isnull()
df.isnull().sum()
df['show_name']=df[ 'show_name'].fillna(df['aired_on'].mode()[0]) 
df['aired_on']=df['aired_on'].fillna(df['aired_on']. mode()[0]) 
df[ 'original_network' ]=df[ 'original_network'].fillna (df['aired_on'].mode()[0]) 
df.head()
df['rating']=df['rating'].fillna(df['rating'].mean())
df['current_overall_rank']=df[ 'current_overall_rank'].fillna (df['current_overall_rank'].mean())
df.head()
df[ 'watchers']=df[ 'watchers'].fillna (df['watchers'].median()) 
df.head()
df.info()
df.isnull().sum()