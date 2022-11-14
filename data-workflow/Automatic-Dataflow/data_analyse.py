import pandas as pd
import os
import matplotlib.pyplot as plt

df = pd.read_csv('./data.csv')
#replacing , with spaces in column names
df.columns = [col.replace(',',' ') for col in df.columns]

#converting dtypes of columns
def object_to_time(obj):
    return pd.to_datetime(obj,format='%Y%m%d %H%M%S')

df['time'] = df['time'].map(object_to_time)
df['El Rio'] = df['El Rio'].astype('int64')
print(df.head())

print(f'Shape {df.shape}')
print(f"Dataset begon op {df['time'][0]} tot {df['time'][len(df['time'])-1]}")
describe = df.describe()
# display(describe)
df = df.drop('Mount Mara VR',axis=1)
describe = describe.drop('Mount Mara VR',axis=1)
print(f"Langste maximale wachttijd ooit: Oki Doki {describe.iloc[7].max()} min")
print(f"Korste maximale wachttijd ooit: Speedy Bob {describe.iloc[7].min()} min")
print(f'Kortste gemiddelde wachttijd: El Rio {describe.iloc[1].min()} min')
print(f'Langste gemiddelde wachttijd: Typhoon {describe.iloc[1].max()} min')
None if os.path.exists('statistieken.txt') else open('statistieken.txt','w')
f = open('statistieken.txt','r+')
f.write(f"Langste maximale wachttijd ooit: Oki Doki {describe.iloc[7].max()} min\n")
f.write(f"Korste maximale wachttijd ooit: Speedy Bob {describe.iloc[7].min()} min\n")
f.write(f'Kortste gemiddelde wachttijd: El Rio {describe.iloc[1].min()} min\n')
f.write(f'Langste gemiddelde wachttijd: Typhoon {describe.iloc[1].max()} min\n')

None if os.path.exists('graphs') else os.mkdir('graphs')
for column in df.drop('time',axis=1).columns:
    df.plot(x='time',y=column,kind='line',figsize=(15,5))
    plt.savefig(f'./graphs/{column.replace(" ","_")}.png')
    # plt.show()

for column in df.drop('time',axis=1).columns:
    df[column][df[column] != 0].value_counts().sort_index().plot(kind='bar',figsize=(15,5),title=column,xlabel='wachttijd(min)',ylabel='Count')
    plt.savefig(f'./graphs/{column.replace(" ","_")}_wt_count.png')
    # plt.show()
