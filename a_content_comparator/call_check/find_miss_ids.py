#!/usr/bin/python
import json
import urllib2
import time
import csv
import call_check.access


class FindMissingIds:

    # input_file = 'valid_assets.json'
    def __init__(self,id_dict, base_dir):
        self.dict = id_dict
        self.base_dir = base_dir

    def url_json(self):
        i = 0
        url_list = []
        d = self.dict
        ids_lenghth = len(d["ids"])
        while i < ids_lenghth:
            id = d["ids"][i]["id"]["id"]
            url = 'https://some_url?withAlternativeIdentifiers=id:{}'.format(id)
            url_list.append(url)
            i += 1
        return url_list

    def magcall(self, urls):
        failed_url = 0
        tested_assets = 0
        missing_p_id = 0
        nb_of_valid = 0
        nb_of_invalid = 0
        nowtime = time.strftime("%Y%m%dT%H%M%S")
    

        csv_path = '{}/output/all_tested_assets-{}.csv'.format(self.base_dir, nowtime)
        with open(csv_path, 'a') as csvfile:
            writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
            writer.writerow(
                ['TITLE', 'ID', 'parentID', 'rootID', 'mediaId', 'currentID', 'availability'])
        for url in urls:
            time.sleep(0.5)
            try:
                json_data = urllib2.urlopen(url).read()
                data = json.loads(json_data)
                keys = jou_call.key_access.Keys(data, url)
                availabilityEndDate = keys.availabilityEndDate()
                if nowtime < availabilityEndDate:
                    nb_of_valid += 1
                    # Loop here if necessary: for d['contents'][i]['bla']
                    title = keys.title()
                    id = keys.id()
                    parentId = keys.parentId()
                    rootId = keys.rootId()
                    GroupId = keys.GroupId()
                    cProductIds = keys.currentProductIds()
    
                    metadata = [title, id, parentId, rootId, GroupId, cProductIds, availabilityEndDate]
    
                    with open(csv_path, 'a') as csvfile:
                        writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL,
                                            lineterminator='\n')
                        writer.writerow(metadata)
                    if not cProductIds:
                        missing_p_id += 1
                else:
                    nb_of_invalid += 1
    
            except:
                # print("URL could not be loaded: ", url)
                failed_url += 1
        print("Job done.")
        print(missing_p_id, " assets missing Product ID for ", nb_of_valid, " assets tested")
        print(nb_of_invalid, " expired assets were found")
        print(failed_url, " API calls were not sucessfull")
