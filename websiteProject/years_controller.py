import cherrypy
import re, json
from terrorism_library import _terrorism_database

class YearsController():
    def __init__(self, tdb):
        self.tdb = tdb

    def GET_KEY(self, year):

        output = {'result': 'success'}

        try:
            output['data'] = self.tdb.getYearDict(int(year))
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)

        return json.dumps(output)