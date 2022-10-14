import hashlib
import time
import warnings
from xml.dom.minidom import Attr
warnings.filterwarnings("ignore",category=FutureWarning)
import json
import requests
import pandas as pd
#import response

timestamp = time.time()
Public_key = 'f8a7866fce794cf586f90aa6c82404b2'
Private_key = 'd455aeca14751cf267e55a3cc9eeaf58426e0770'

def hashing():
    md5hash = hashlib.md5()
    md5hash.update(f'{timestamp}{Private_key}{Public_key}'.encode('utf-8'))
    hashedparam = md5hash.hexdigest()

    return hashedparam

def newfunc(key_api,hash,name_starts_with=None):
    if not key_api and not hash:
        raise AttributeError("Missing API key and Hash value!")
    elif not key_api:
        raise AttributeError("Missing API Value")
    elif not hash:
        raise AttributeError("Missing hash value")
    #print(response.raise_for_status())
    timestamp1 = time.time()
    df = pd.DataFrame()

    for i in range (3):
        headers2 = {'ts':timestamp1, 'apikey':Public_key,'hash':hashing(),'limit':100,'nameStartsWith':name_starts_with,'offset':100*i}
        req2 = requests.get('https://gateway.marvel.com/v1/public/characters',params=headers2,verify=False).json()
        data = req2['data']['results']
        df2 = pd.json_normalize(data)
        df = df.append(df2,ignore_index=True)

    return df[['name','events.available','series.available','stories.available','comics.available','id']]

#print(newfunc(","))
print(newfunc(Public_key,hashing(),"Spider"))
    