import cherrypy
import re, json
from terrorism_library import _terrorism_database

class CountriesController():
    def __init__(self, tdb):
        self.tdb = tdb

    def GET_KEY(self, country):

        output = {'result': 'success'}

        try:
            output['data'] = self.tdb.getCountryDict(country)
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)

        return json.dumps(output)