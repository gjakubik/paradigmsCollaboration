import cherrypy
import re, json
from terrorism_library import _terrorism_database

class EventController():
    def __init__(self, tdb):
        self.tdb = tdb

    def GET_KEY(self, eventid):

        output = {'result': 'success'}

        try:
            output['data'] = self.tdb.getEventDict(eventid)
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)

        return json.dumps(output)

    def GET_INDEX(self):

        output = {'result': 'sucess'}

        try:
            output['data'] = self.tdb.db
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)
        
        return json.dumps(output)
            