import json
import glob
import os
from collections import OrderedDict

path = '/home/nrw/ED/sample_data_20190318/*.log'
file_list = glob.glob(path)
latest_entry = max(file_list, key=os.path.getctime)
print(latest_entry)





# Return Wanted Data as json object. e.g input param "Location" to get system info #
# Note:  Return the object of interest based on the type of events and what to_track inside an event list #
def json_obj(interest, events, path, to_track):

    with open(path, 'r') as f:

        if interest == "INFLUENCE":
            for line in f:
                if any(event in line for event in events) and to_track in line: # Elegant way to do: if event[0] in line and event[i] in line:
                    data = json.loads(line)

        if interest == "SYS_INFO":
            for line in f:
                if any(event in line for event in events):
                    data = json.loads(line)
        f.close()
        return data



def influence_tracker(loc_data):

    d = {}
    i = 0

    while i < len(loc_data["Factions"]):
        d[loc_data["Factions"][i]["Name"]] = loc_data["Factions"][i]["Influence"]
        i += 1

    d = {k: v for k, v in sorted(d.items(), key=lambda x: x[1])} #sort dict
    for i in d:
        if d[i] != 0:
         print(i, d[i]*100,'%')



def sys_info(loc_data):

    sys_info_txt = "{} controlled by {} \n" \
                   "Economy: {} and {} \n"\
                   "Government: {} \n" \
                   "Security: {} \n" \
                   "Population: {}".format(loc_data["StarSystem"], loc_data["SystemAllegiance"],
                                               loc_data["SystemEconomy_Localised"],
                                               loc_data["SystemSecondEconomy_Localised"], loc_data["SystemGovernment_Localised"], loc_data["SystemSecurity_Localised"], loc_data["Population"])
    return sys_info_txt


sys_input = 'AR100'
sys_to_track = '"StarSystem":"{}"'.format(sys_input)
per_system_data = json_obj('INFLUENCE', ['Location', 'FSDJump'], latest_entry, sys_to_track)
latest_system_data = json_obj('SYS_INFO', ['Location', 'FSDJump'], latest_entry, '')

influence_tracker(per_system_data)
sys_info(latest_system_data)

