import pandas as pd 
import numpy as np
import itertools

class _terrorism_database():

    def __init__(self, filename):
        
        self.loadData(filename)

    def loadData(self, filename):
        df = pd.read_csv(filename, low_memory=False)
        df.drop(columns=dropCols, inplace=True)
        df.set_index("eventid", inplace=True)
        df.fillna(0)
        self.db = df.to_dict('index')
        
        self.byCountry = df.groupby('country_txt')
        self.byYear = df.groupby('year')

    def getEventDict(self, eventid):
        if int(eventid) in self.db:
            return self.db[int(eventid)]
        return None
    def getCountryDict(self, country):
        return self.byCountry.get_group(country).to_dict('index')

    def getYearDict(self, year):
        return self.byYear.get_group(year).to_dict('index') 

        
    
dropCols = [
            "attacktype3",
            "attacktype3_txt",
            "corp1",
            "target1",
            "targtype2",
            "targtype2_txt",
            "targsubtype2",
            "targsubtype2_txt",
            "corp2",
            "target2",
            "natlty2",
            "natlty2_txt",
            "targtype3",
            "targtype3_txt",
            "targsubtype3",
            "targsubtype3_txt",
            "corp3",
            "target3",
            "natlty3",
            "natlty3_txt",
            "gsubname",
            "gname2",
            "gsubname2",
            "gname3",
            "gsubname3",
            "motive",
            "guncertain2",
            "guncertain3",
            "claim2",
            "claimmode2",
            "claimmode2_txt",
            "claim3",
            "claimmode3",
            "claimmode3_txt",
            "compclaim",
            "propcomment",
            "addnotes",
            "scite1",
            "scite2",
            "scite3",
            "dbsource",
            "INT_LOG",
            "INT_IDEO",
            "INT_MISC",
            "INT_ANY"
        ]