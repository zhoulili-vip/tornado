import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.wsgi
from wsgiref import simple_server
from tornado.options import define, options

define("port", default=80, help="run on the given port", type=int)
define("host", default='192.168.1.101', help="run on the given host")

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, tornado")

wsgi_test_local = True
if __name__ == "__main__" and not wsgi_test_local:
    application = tornado.web.Application([(r"/", MainHandler)])
else:
    application = tornado.wsgi.WSGIApplication([(r"/", MainHandler)])


def handler(environ, start_response):
    """
    在阿里云上用“函数计算”功能运行tornador
    所有的异步计算将转化为同步计算并返回结果
    “函数计算”是阿里云上最低成本测试web的服务，使用HTTP触发器
    :param environ:
    :param start_response:
    :return:
    """
    return application(environ, start_response)


def main_test_async():
    """
    本地测试tornado异步功能，当“函数计算”性能不够时使用“轻量应用服务器”部署
    :return:
    """
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port, options.host)
    tornado.ioloop.IOLoop.current().start()

def main_test_wsgi():
    """
    本地测试wsgi功能，上传阿里云“函数计算”之前本地测试
    :return:
    """
    server = simple_server.make_server(options.host, options.port, application)
    server.serve_forever()


if __name__ == "__main__":
    if wsgi_test_local:
        main_test_wsgi()
    else:
        main_test_async()
