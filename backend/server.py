import tornado.ioloop
import tornado.web
import tornado.httpserver
import tornado.process
import tornado.netutil
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
    httpsock = tornado.netutil.bind_sockets(config.PORT)
    tornado.process.fork_processes(config.PROCESSES)
    app = tornado.web.Application([
        ('/',IndexHandler),
        ('/(.*)', tornado.web.StaticFileHandler, {'path': config.STATIC_FILE_DIR}),
        ], cookie_secret=config.COOKIE_SECRET, autoescape='xhtml_escape')
    srv = tornado.httpserver.HTTPServer(app)
    srv.add_sockets(httpsock)
    tornado.ioloop.IOLoop.instance().start()
