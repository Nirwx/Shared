import requests
from collections import defaultdict
from mongo import MongoConnection
import time
from datetime import datetime, timedelta
import json
from bson.json_util import dumps


# Fetch and Store information from the API
class MetroApiOperations:
#Fecth version information and build the URL accordingly if version has changed since the previous check
    def __init__(self):

        self.mongoconnection = MongoConnection()
        dataDB = self.mongoconnection.find_one('store_info')
        req = requests.get(***STORE_URL***)
        dataAPI = req.json()
        # See if Store Version has been updated
        if dataDB["storeHash"] == dataAPI["storeHash"] and dataDB["storeVersion"] == dataAPI["version"]:
            self.d = dataDB
        else:
            store_url = '***BASE METADATA URL***'.format(dataAPI["storeHash"], dataAPI["version"])
            req = requests.get(store_url)
            self.d = self.build_app_dict(req.json(), dataAPI["storeHash"], dataAPI["version"], store_url)
            self.mongoconnection.insert_one('store_info', self.d)

#Structure Data to be stored
    def build_app_dict(self, appStoreData, storeHash, storeVersion, store_url):

        d = defaultdict(dict)
        inner_d = defaultdict(dict)
        nb_of_category = len(appStoreData[1]["data"])
        i = 0
        y = 0

        while i < nb_of_category:
            for cat_d in appStoreData[1]["data"][i]["data"]:
                inner_d[str(y)]["name"] = cat_d["name"]
                inner_d[str(y)]["url"] = 'https:{}'.format(cat_d["url"])
                y += 1
            i += 1

        d["storeHash"] = storeHash
        d["storeVersion"] = storeVersion
        d["storePath"] = store_url
        d["store_last_check"] = datetime.now()
        d["data"] = inner_d
        return d


    # Test URL status code for the entire Apps Dictionnary and write status code in DB
    def test_response(self):

        del self.d["_id"]
        for i in self.d["data"]:
            url = self.d["data"][i]["url"]
            req = requests.get(url)
            resp_code = req.status_code
            self.d["data"][i]["status"] = resp_code
            self.d["data"][i]["last_check"] = int(time.time() * 1000) # Epoch time in MS req. by Grafana
        self.d["insert_time"] = datetime.now()
        self.mongoconnection.insert_one('http_response', self.d)
        return self.d["data"]

#Fetch Status Data and structure to display in Grafana
class getResponseData():

    def structure_data(self):
        mongoco = MongoConnection()
        now = datetime.now()
        date = datetime.now() - timedelta(
            days=30)  # placeholder, define date of data to poll (and display on Grafana) Tweak to extend/shrink date range in return response
        d = defaultdict(dict)
        y = 0
        for doc in mongoco.find_time_range('http_response', date, now):
            for i in doc["data"]:
                d["data"][str(y)] = doc["data"][str(i)]
                y += 1

        i = 0
        rows = ''
        while i < len(d["data"]):
            time = d["data"][str(i)]["last_check"]
            app_name = d["data"][str(i)]["name"]
            status = d["data"][str(i)]["status"]
            if i + 1 == len(d["data"]):
                row = '[{},"{}",{}]'.format(time, app_name, status)
            else:
                row = '[{},"{}",{}],\n'.format(time, app_name, status)
            rows += row
            i += 1

        grafana_json = '''[
          {
            \"columns\":[
              {\"text\":\"Time\",\"type\":\"time\"},
              {\"text\":\"App\",\"type\":\"string\"},
              {\"text\":\"Status\",\"type\":\"number\"}
            ],
            \"rows\":[ ''' + rows + '''
            ],        
            \"type\":\"table\"
          }
        ]'''
        return grafana_json
