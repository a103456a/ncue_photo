import json
import os


def loadData():
    DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    with open(os.path.join(DIR, "json\\navbar_item.json"), encoding='utf-8') as data_file :    
        data = json.load(data_file)
        
    return data