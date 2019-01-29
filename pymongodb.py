from pymongo import MongoClient
from bson import json_util
import tornado.ioloop
import tornado.web
#-*- coding:utf-8 -*-
class MainHandler(tornado.web.RequestHandler):
    def set_default_header(self):
        # 后面的*可以换成ip地址，意为允许访问的地址
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Headers', 'x-requested-with')
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, PUT, DELETE')

    def get(self):
        client = MongoClient(host="localhost", port=27017)
        collection = client["student"]["chemical"]
        ret = collection.find()
        new_list = []
        for i in ret:
            new_list.append(i)
            print(i)
        result_dict = dict()
        result_dict['data'] = new_list
        r=json_util.dumps(result_dict,ensure_ascii=False)

        self.write(r)

def make_app():
    return tornado.web.Application([
        (r"/content", MainHandler)
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8801)
    tornado.ioloop.IOLoop.current().start()

