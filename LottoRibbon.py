import folium
import pandas as pd

map_folium = folium.Map(location=[35.8778558, 128.6045069], zoom_start=11)
map_folium

map_folium.save('index.html')

# use csv file, create dataframe
file = 'C:/Users/ab1t3/Downloads/lotto.csv'
raw = pd.read_csv(file, encoding='cp949')
raw.head()
raw.info()

for i in range(len(raw)):
    lat = raw.loc[i, '위도']
    long = raw.loc[i, '경도']
    name = raw.loc[i, '복권판매점']
    num = raw.loc[i, '1등당첨횟수']
    
    print(name, lat, long, num)

