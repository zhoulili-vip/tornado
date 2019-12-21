import tornado.web
import tornado.wsgi


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, tornado")


application = tornado.wsgi.WSGIApplication([(r"/", MainHandler)])


def handler(environ, start_response):
    return application(environ, start_response)

