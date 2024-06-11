import requests
import json
import time
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Requesting and reading response from API for current weather data
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
sns.set_style('white')
sns.lineplot(x="Hour", 
            y="Temp in C",
            data=df).set(
                title="Temperature for 24 hours today",
                xlabel="Time",
                ylabel="Temperature",
            )
plt.show()

#weather for the next 14 days
response_API = requests.get('http://api.weatherapi.com/v1/forecast.json?key=fb0bc518316645c4b10114248240306&q=13.03,80.26&days=14&aqi=no&alerts=no')
data = json.loads(response_API.text)

#dumping raw API data
with open ('api_data.json','w') as f:
    json.dump(data,f)

#processing api data and converting it to a dataframe
date=[]
temps=[[],[],[]]
current_activity = data['forecast']['forecastday']
parameters = ["maxtemp_c","mintemp_c","avgtemp_c"]
for i in range(14):
    date.append(data['forecast']['forecastday'][i]['date'])
    temps[0].append(current_activity[i]['day']['maxtemp_c'])
    temps[1].append(current_activity[i]['day']['mintemp_c'])
    temps[2].append(current_activity[i]['day']['avgtemp_c'])

df = pd.DataFrame({'Date':date, 'Max_temp':temps[0], 'Min_temp':temps[1],'Avg_temp':temps[2]})
df.to_excel('output.xlsx')

sns.set_style('white')
sns.lineplot(x="Date", 
            y="Avg_temp",
            data=df).set(
                title="Average temperature for the next 14 days",
                xlabel="Date",
                ylabel="Average Temperature",
            )
plt.show()

#visualizing the data
sns.scatterplot(
    data = df, x='Min_temp', y='Max_temp'
    ).set(
        title="Minimum vs Maximum Temperature",
        xlabel="Minimum Temperature",
        ylabel="Maximum Temperature",)

plt.show()