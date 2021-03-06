import cherrypy
import json

class DictionaryController(object):
    # this is a controller class, which holds event handlers
    # constructor
    def __init__(self):
        self.myd = dict()

    def get_value(self, key):
        return self.myd[key]

    def add_entry(self, key, value):
        self.myd[key] = value

    # event handlers for resource requests
    def GET_KEY(self, key):
        output = {'result' : 'success'} # 1.
        key = str(key) # 2.

        try:
            house = self.get_value(key)
            if house is not None:
                output['key'] = key
                output['value'] = house
            else:
                output['result'] = 'error'
                output['message'] = 'None type value associated with requested key'
        except KeyError as ex:
            output['result'] = 'error'
            output['message'] = 'key not found'
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)

        return json.dumps(output)

    def PUT_KEY(self, key):
        # 1. create a default response object 
        output = {'result' : 'success'}
        key = str(key) # 2. cast the input into the desired type
        # 3. (only for body)get body of message
        data_json = json.loads(cherrypy.request.body.read())

        # 4. do the work in try-except block(s)
        try:
            val = data_json['value'] # grab the value in the message
            self.add_entry(key, val) # actual update happens here
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)
        # 5. return the string response
        return json.dumps(output)

    def GET_INDEX(self):
        output = {'result': 'success'}

        output['entries'] = [{'key': entry, 'value': self.myd[entry]}for entry in self.myd.keys()]

        return json.dumps(output)

    def POST_INDEX(self):
        output = {'result': 'success'}

        data_json = json.loads(cherrypy.request.body.read())

        try:
            key = data_json['key']
            val = data_json['value']
            self.add_entry(key, val)
        except Exception as e:
            output['result'] = 'failure'
            output['message'] = str(e)
        
        return json.dumps(output)

    def DELETE_KEY(self, key):
        output = {'result': 'success'}

        # returns none if key not found
        removed_key = self.myd.pop(str(key), None)
        if removed_key == None:
            output['result'] = 'failure'
            output['message'] = 'key not found'
        
        return json.dumps(output)

    def DELETE_INDEX(self):
        self.myd.clear()
        return json.dumps({'result': 'success'})