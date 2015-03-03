import tornado.ioloop
import tornado.web
import tornado.httpserver
from req import Service
from req import reqenv
from req import RequestHandler
import config
import pg

class IndexHandler(RequestHandler):
    @reqenv
    def get(self):
        self.render('index.html')
        return

if __name__ == '__main__':
    app = tornado.web.Application([
        ('/',IndexHandler),
        ('/(.*)', tornado.web.StaticFileHandler, {'path': config.STATIC_FILE_DIR}),
        ], cookie_secret=config.COOKIE_SECRET, autoescape='xhtml_escape')
    srv = tornado.httpserver.HTTPServer(app)
    srv.bind(config.PORT)
    srv.start(config.THREADS)
    tornado.ioloop.IOLoop.instance().start()
