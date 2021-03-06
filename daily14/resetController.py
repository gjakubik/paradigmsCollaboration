import cherrypy
import re, json
from movies_library import _movie_database

class ResetController(object):

    def __init__(self, mdb=None):
        if mdb is None:
            self.mdb = _movie_database()
        else:
            self.mdb = mdb


    def PUT_INDEX(self):
        '''when PUT request comes in to /reset/ endpoint, then the movie database is reloaded'''
        output = {'result':'success'}

        data = json.loads(cherrypy.request.body.read().decode())

        self.mdb.__init__()
        self.mdb.load_movies('movies.dat')
        self.mdb.load_ratings('ratings.dat')

        return json.dumps(output)

    def PUT_KEY(self, movie_id):
        '''when PUT request comes in for /reset/movie_id endpoint, then that movie is reloaded and updated in mdb'''
        output = {'result':'success'}
        mid = int(movie_id)

        try:
            data = json.loads(cherrypy.request.body.read().decode())

            mdbtmp = _movie_database()
            mdbtmp.load_movies('movies.dat')

            movie = mdbtmp.get_movie(mid)
            
            # sets movie and genre in movies_library.py
            self.mdb.set_movie(mid, movie)

        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)

        return json.dumps(output)
