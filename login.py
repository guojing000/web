import json
from pymongo import MongoClient
import pprint
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
    def post(self):
        #连接到数据库
        conn = MongoClient(host="localhost", port=27017)    #connect to mongodb
        db= conn["users"]["users_collection"]
        # name=input('请输入用户名：')
        # password=input('请输入密码：')
        name = self.get_argument("username")
        password = self.get_argument("password")
        # print(name,type(name))
        array=db.find()
# pprint.pprint(array)
        new_list = []
        d=[]
        for r in array:
            new_list.append(r)
    # print(r, type(r))
        #     # lst_keys , lst_values = r.keys(), rz.values()
        #      # print(lst_keys , lst_values,type(lst_keys))
            new_list1 = []
            for name1 in r['name']:
                new_list1.append(name1)
        #     # print(new_list1,type(new_list1))
                new_list2 = ''.join(new_list1)

    # print(new_list2, type(new_list2))
            new_list3 = []
            for password1 in r['password']:
                new_list3.append(password1)
            new_list4 = ''.join(new_list3)
    # print(new_list4,type(new_list4))
        # # result_dict = dict()
        # # result_dict['data'] = new_list
        #

            if (name == new_list2)&(password == new_list4):
            # self.write("用户登录成功")
                v='1'

            else:
                v='0'
        #         self.write("用户登录失败")
    # print(v)

            d.append(v)
        # print(d)

    # o=[]
    # o=''.join(d)
    # print(o,type(o))
    # d = ''.join(v)
    #     # print(v,type(v))
    # print(d)
        if '1'in d:
    # print('c')
            self.write("用户登录成功")
        else:
    # print('s')
            self.write("用户登录失败")
    #         self.render(info={'status':False,
    #                            'info':'用户登录失败',
    #                             'second':3,
    #                             'url':r'/login'})







# array = list(db.find())
# pprint.pprint(array)








# result_dict = dict()
# result_dict['data'] = new_list
# r = json_util.dumps(result_dict, ensure_ascii=False)
# c=tuple(r)
# print(result_dict)
# for l in result_dict.keys():
#     # for item in l:
# #     #     print(item)
# print(l,result_dict[l])

# def get(a):
#     if a in list(r):
#         print("ship")
#
#     else:
#         print("chengg")

# print(array,type(array))
        # if r.name==a:
        #         self.write("用户名存在，请重新输入用户名")
        #
        #         #增加一个document
        # else:
        #         insert_user = [{"name":"{}".format(i),"password":"{}".format(j)}for i in a for j in b ]
        #         db.users_collection.insert(insert_user)
        # #print(db.users_collection)
        # #print("after inserting:")
        #         array = list(db.users_collection.find())
        # #pprint.pprint(array)
        #         self.write("注册成功")



def make_app():
        return tornado.web.Application([
            (r"/login", MainHandler)
        ])

if __name__ == "__main__":
        app = make_app()
        app.listen(8880)
        tornado.ioloop.IOLoop.current().start()