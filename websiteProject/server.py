import cherrypy
from terrorism_library import _terrorism_database
from events_controller import EventController
from countries_controller import CountriesController
from years_controller import YearsController

def start_server():
    dispatcher = cherrypy.dispatch.RoutesDispatcher()

    tdb = _terrorism_database('terrorismData.csv')

    eventController = EventController(tdb)
    countriesController = CountriesController(tdb)
    yearsController = YearsController(tdb)

    dispatcher.connect('event_index_get', '/events/', controller=eventController, action='GET_INDEX', conditions=dict(method=['GET']))
    dispatcher.connect('event_get', '/events/:eventid', controller=eventController, action='GET_KEY', conditions=dict(method=['GET']))
    dispatcher.connect('country_get', '/countries/:country', controller=countriesController, action='GET_KEY', conditions=dict(method=['GET']))
    dispatcher.connect('year_get', '/years/:year', controller=yearsController, action='GET_KEY', conditions=dict(method=['GET']))

    conf = {
	'global': {
        'server.thread_pool': 5, # optional argument
	    'server.socket_host': 'localhost', # 
	    'server.socket_port': 51068, #change port number to your assigned
	    },
	'/': {
	    'request.dispatch': dispatcher,
	    }
    }

    cherrypy.config.update(conf)
    app = cherrypy.tree.mount(None, config=conf)
    cherrypy.quickstart(app)


if __name__ == "__main__":
    start_server()
