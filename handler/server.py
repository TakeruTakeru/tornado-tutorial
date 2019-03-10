from .MainHandler import SimpleApplication
import tornado.ioloop

if __name__ == '__main__':
    app = SimpleApplication()
    app._application.listen(8888)
    tornado.ioloop.IOLoop.current().start()