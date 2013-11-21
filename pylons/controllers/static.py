from pylons.controllers import WSGIController
from fanstatic import LibraryRegistry, Publisher
import webob

__all__ = ['FanstaticController']

class FanstaticController(WSGIController):

    def __call__(self, environ, start_response):
        request = webob.Request(environ)

        ignored = request.path_info_pop()
        while request.path_info.lstrip('/') != environ['pylons.routes_dict']['file']:
            ignored = request.path_info_pop()

        publisher = Publisher(LibraryRegistry.instance())
        return publisher(environ, start_response)
