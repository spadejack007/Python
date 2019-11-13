'''
1、调用connect()方法打开数据库连接，该方法返回数据库连接对象
2、通过数据库连接对象打开游标
3、使用游标执行SQL语句(包含DDL、DML、select查询语句等)
4、关闭游标
5、关闭数据库连接
6、本例子练习了a、数据库连接、b、执行语句、d、执行多条插入、d、执行多次获取、e、sqlite自定义函数 f、自定义聚集函数
***************
1、python如果只带一个元素的元组，元素后面要加一个","  逗号。 
2、DML语句(Data Manipulation Language)：用于增删改表中数据，DML是伴随TCL事务控制的。
3、DDL语句(Data Definition Language)：数据定义语言，用来维护数据库对象 
4、rowcount属性在update语句后面才会返回行数，默认是-1
'''
import sqlite3

#1、打开或创建数据库
conn = sqlite3.connect('first.db')
#2、获取游标
c = conn.cursor()
#3、执行语句
#***3.1、3.2、3.3多个章节的语句可以逐次打开执行***#
#3.1数据库DDL语句，创建user_tb、order_tb两个表
create_user_tb_SQL = '''create table user_tb(_id integer primary key autoincrement,
name text,
pass text,
gender text)'''
create_order_tb_SQL = '''create table order_tb(_id integer primary key autoincrement,
item_name text,
item_price real,
item_number real,
user_id integer,
foreign key(user_id) references user_tb(_id))'''
#c.execute(create_user_tb_SQL)
#c.execute(create_order_tb_SQL)

#3.2执行插入语句
#c.execute('insert into user_tb (name,pass,gender) values ("孙悟空","123456","male")')
#c.execute('insert into order_tb (item_name,item_price,item_number,user_id) values ("鼠标",34.2,3,1)')
#conn.commit()

#3.3执行多行插入
#insertManyList = (("sun","123456","male"),("bai","123456","female"),("zhu","123456","male"))
#c.executemany('insert into user_tb (name,pass,gender) values (?,?,?)',insertManyList)#此处用了占位符"?"
#conn.commit()

#3.4执行获取数据并逐行呈现
'''c.execute('select * from user_tb where _id > 1')
#print('查询返回的记录数：',c.rowcount)
#通过游标的descritpion属性获取列信息
for col in (c.description):
    print(col[0],end = '\t')
print('\n','*'*30)
while True:
    row = c.fetchone()
    if not row:
        break
    print(row)
    print(row[1]+'---->'+row[2])'''

#3.5执行创建自定义函数
'''#使用自定义函数。场景：可以用于密码加密
def reverse_ext(st):
    return '['+st[::-1]+']'#st[::-1]是对字符串进行取反；
#数据库连接对象提供的create_function(name,num_params,func)方法
#a、name参数：指定注册的自定义函数的名字
#b、num_params参数：自定义函数所需要的参数数量
#c、func参数：指定自定义函数对应的函数
conn.create_function('enc',1,reverse_ext)#注意：create_function第一个函数的别名需要用单引号，第三个参数的函数名不需要单引号
c.execute('insert into user_tb (name,pass,gender) values (?,enc(?),?)',('贾宝玉','123456','male'))
conn.commit()'''

#3.6执行创建聚集函数
#数据库连接对象提供的create_aggregate(name,num_params,aggregate_class)
#a、name参数：指定注册的自定义聚集函数的名字
#b、num_params参数：自定义聚集函数所需要的参数数量
#c、aggregate：指定聚集函数的实现类。该类必须实现step(self,params...)和finalize(self)
#   其中step函数对于查询所返回的每条记录各执行一次；
#   其中finalize只在最后执行一次，该方法的返回值作为聚集函数的返回值
#class--定义聚集类
class MinLen:
    def __init__(self):
        self.min_len = None
    def step(self,value):
        if(self.min_len is None):
            self.min_len = value
            return
        if(self.min_len > value):
            self.min_len = value
    def finalize(self):
        return self.min_len
conn.create_aggregate('min_len',1,MinLen)
c.execute('select min_len(pass) from user_tb')
print(c.fetchone()[0])
conn.commit()
#4、关闭游标
c.close()
#5、关闭连接
conn.close()