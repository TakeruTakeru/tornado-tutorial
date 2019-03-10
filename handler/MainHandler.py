import tornado.ioloop
import tornado.web
from logging import getLogger, INFO
import json
from pprint import pprint
from datetime import datetime

logger = getLogger(__package__)
logger.setLevel(INFO)

debug_json = {
    'code': 200,
    'response': 'ok'
}

class MainHandler(tornado.web.RequestHandler):

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def get(self):
        obj = {
            'code': 200,
            'response': 'ok'
        }
        self.set_header('Content-Type', 'application/json')
        json_content = json.dumps(obj, ensure_ascii=False)
        self.write(json_content)
        logger.info(self.request)
        self.flush()

    def post(self):
        self.set_header('Content-Type', 'application/json')
        self.write(json.dumps(debug_json, ensure_ascii=False))

    # def options(self):
    #     self.set_status(204)
    #     self.finish()

    def prepare(self):
        print(self.request)


class StoryHandler(tornado.web.RequestHandler):
    def get(self, story_id):
        self.write("You requested the story " + story_id)


class ProfileHandler(tornado.web.RequestHandler):
    def initialize(self, database):
        self.database = database

    def get(self, username):
        logger.info(username)
        # arg = self.get_argument()
        # print(arg)
        # param = self.get_user_locale()
        # print(param)
        # pprint(self.__dict__)

    def post(self):
        self.set_header("Content-Type", "text/plain")
        # self.write("You wrote " + self.get_argument("message"))


def create_msg(*args):
    now = datetime.now()
    return now.strftime('[%Y/%m/%d %H:%M:%S]{}'.format('params => ')) + ' '.join(args)


database = []
application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/story/([0-9]+)", StoryHandler),
    (r'/user/(.*)', ProfileHandler, dict(database='database')),
])


class SimpleApplication:
    def __init__(self):
        self._application = application


if __name__ == '__main__':

    application.listen(8888)

    tornado.ioloop.IOLoop.current().start()
