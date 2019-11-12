import requests
from collections import defaultdict
from mongo import MongoConnection
import time
from datetime import datetime, timedelta
import json
from bson.json_util import dumps



class MetroApiOperations:

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


    # Test URL status code for the entire Apps Dictionnary
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


class getResponseData():

    def __init__(self):
        mongoco = MongoConnection()
        now = datetime.now()
        date = datetime.now() - timedelta(days = 7)
        self.d = {}
        for doc in mongoco.find_time_range('http_response', date, now):
            self.d.update(doc)
        print(self.d)
        #self.d = mongoco.find_one('http_response')


    def structure_data(self):
        i = 0
        rows = ''
        while i < len(self.d["data"]):
            time = self.d["data"][str(i)]["last_check"]
            app_name = self.d["data"][str(i)]["name"]
            status = self.d["data"][str(i)]["status"]
            if i+1 == len(self.d["data"]):
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


    #test_response(global_dict)

