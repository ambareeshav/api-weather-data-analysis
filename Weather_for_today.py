import requests
import json
import time
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Requesting and reading response from API for current weather data
#current weather
#response_API = requests.get('http://api.weatherapi.com/v1/current.json?key=fb0bc518316645c4b10114248240306&q=13.036791,80.267632&aqi=no')

#weather on a specific day
#response_API = requests.get('http://api.weatherapi.com/v1/forecast.json?key=fb0bc518316645c4b10114248240306&q=13.03,80.26&dt=2023-12-15')

response_API = requests.get('http://api.weatherapi.com/v1/forecast.json?key=fb0bc518316645c4b10114248240306&q=13.03,80.26dt=2023-01-10&aqi=no&alerts=no')
data = json.loads(response_API.text)

#dumping raw API data

with open ('api_data.json','w') as f:
    json.dump(data,f)
    
#Choosing values to use and
#Converting json data to a dataframe and also copying the data to a excel file 
current_activity = data['forecast']['forecastday'][0]['hour']
df = pd.DataFrame.from_dict(current_activity, orient='columns')

#splitting time column into date and time
df[['Date','Hour']] = df.time.str.split(" ",expand=True)
df.drop(['time'],axis=1,inplace=True)
df.rename(columns={'temp_c':'Temp in C'}, inplace=True)
df.to_excel('output.xlsx')

#Visulaizing temperature throughout the day
def vis():
    sns.set_style('white')
    #sns.distplot(df, kde=True,color='b')
    #sns.lineplot(df['temp_c'])
    sns.lineplot(x="Hour", 
                y="Temp in C",
                data=df)
    plt.show()
vis()