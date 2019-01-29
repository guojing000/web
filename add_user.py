
from pymongo import MongoClient
import tornado.ioloop
import tornado.web
#-*- coding:utf-8 -*-
class AddHandler(tornado.web.RequestHandler):
    def set_default_header(self):
        # 后面的*可以换成ip地址，意为允许访问的地址
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Headers', 'x-requested-with')
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, PUT, DELETE')

    def get(self):
        conn = MongoClient(host="localhost", port=27017)
        db= conn["users"]["users_collection"]

        # a=input('请输入用户名：')
        # b=input('请输入密码：')
        name = self.get_argument("username")
        print(name)
        password = self.get_argument("password")
        print(password)
        # email = self.get_argument('email')
        # print(name,type(name))
        array=db.find({},{"name":1})
        #pprint.pprint(array)
        new_list = []
        d = []
        for r in array:
            new_list.append(r)
            # print(r, type(r))
            # lst_keys , lst_values = r.keys(), rz.values()
             # print(lst_keys , lst_values,type(lst_keys))
            new_list1 = []
            for name1 in r['name']:
                new_list1.append(name1)
            # print(new_list1,type(new_list1))
            new_list2 = ''.join(new_list1)
            #print(new_list2, type(new_list2))

        # result_dict = dict()
        # result_dict['data'] = new_list
            if name == new_list2:
                v = '0'
            else:
                v = '1'
# array = list(db.find())
# pprint.pprint(array)

            d.append(v)
        if '0' in d:
                self.write("用户名存在，请重新输入用户名")
        else:
                # insert_user = [{"name": "{}".format(name), "password": "{}".format(password), "email": "{}".format(email)}]
                insert_user = [
                    {"name": "{}".format(name), "password": "{}".format(password)}]
                db.insert(insert_user)
                self.write("注册成功")









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
            (r"/register", AddHandler)
        ])

if __name__ == "__main__":
        app = make_app()
        app.listen(8800)
        tornado.ioloop.IOLoop.current().start()




