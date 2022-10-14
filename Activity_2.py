import requests
import json
from http.client import REQUESTED_RANGE_NOT_SATISFIABLE
import pandas as pd
import time
import hashlib
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

timestamp = time.time()
Public_key = 'f8a7866fce794cf586f90aa6c82404b2'
Private_key = 'd455aeca14751cf267e55a3cc9eeaf58426e0770'

def hashing():
    md5hash = hashlib.md5()
    md5hash.update(f'{timestamp}{Private_key}{Public_key}'.encode('utf-8'))
    hashedparam = md5hash.hexdigest()

    return hashedparam


limit1 = input("Give limit")
name = input("Give starting name")
headers1 = {'ts': timestamp, 'apikey': Public_key,
            'hash': hashing(), 'limit': limit1, 'nameStartsWith': name}

pq = "https://gateway.marvel.com/v1/public/characters"
base_url = "https://gateway.marvel.com"
api_key = Public_key
query = "/v1/public/characters"+"?"

newt = str(timestamp)
query_url = base_url + query + "ts=" + newt + "&apikey=" + api_key + "&hash=" + hashing()

req1 = requests.get('https://gateway.marvel.com/v1/public/characters',params=headers1, verify=False).json()
data = req1['data']['results']

df1 = pd.json_normalize(data)
df1[['name','events.available','series.available','stories.available','comics.available','id']]
print("dynamic",df1)

df11 = pd.DataFrame()

for i in range(3):
    headers2 = {'ts':timestamp, 'apikey':Public_key,'hash':hashing(),'limit':100,'offset':100*i}
    req2 = requests.get('https://gateway.marvel.com/v1/public/characters',params=headers2,verify=False).json()
    data = req2['data']['results']
    df2 = pd.json_normalize(data)
    df11 = df11.append(df2,ignore_index=True)

newd = df11[['name','events.available','series.available','stories.available','comics.available','id']]
print(newd)