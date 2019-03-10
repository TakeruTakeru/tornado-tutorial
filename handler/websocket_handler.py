import tornado.ioloop
import tornado.websocket
from logging import getLogger, INFO
import json
from pprint import pprint
import time

logger = getLogger(__package__)
logger.setLevel(INFO)

class OriginalWebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        logger.info('connection with {}'.format(self.request.remote_ip))
        self.ioloop = tornado.ioloop.IOLoop.instance()
        self.send_websocket()
    
    def on_close(self):
        logger.info('connection is closed.')
    
    def check_origin(self, origin):
        return True

    def on_message(self, message):
        logger.info(message)
        self.write_message(message)

    def send_websocket(self):
        self.ioloop.add_timeout(time.time() + 1, self.send_websocket)
        if self.ws_connection:
            message = json.dumps({'status': 200, 'data': 'okok'})
            self.write_message(message)

application = tornado.web.Application([
    (r"/ws/sample", OriginalWebSocketHandler),
], websocket_ping_interval=1000)

if __name__ == '__main__':

    application.listen(8888)
    
    tornado.ioloop.IOLoop.current().start()