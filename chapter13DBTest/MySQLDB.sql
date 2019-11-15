'''3.1-查看版本和显示当前时间'''
sql = "select version();"
sql = "select now();"
'''3.2-数据库操作'''
show database;
use database_Name;database_Name为数据库名
select database();--database()为数据库的内置函数
create database 数据库名 charset="utf8";
drop database;删除数据库
'''3.2-数据库表操作'''
show tables;
desc 表名;--查看表结构
'''3.2.1创建表'''
create table table_name(
	column1 datatype contrai,
	column2	datatype,
	...
	columnN datatype,
	PRIMARY KEY(one ore more columns)
);
'''3.2.2-修改表'''
--修改表-添加字段
alter table table_name add column2	datatype;
alter table students add birth datetime;
--修改表-修改字段-重命名
alter table table_name change 原名 新名 类型及约束;
alter table students change birth birthday datetime no null;
--修改表-修改字段-不重名版
alter table table_name modify 原名 类型及约束
alter table students modify birthday date not null;
--修改表-删除字段
alter table 表名 drop 列名;
alter table students drop birthday;
'''3.3.3-删除表及其他操作'''
--删除表
drop table 表名;
drop table students;
--查看表的创建语句
show create table 表名;
show create table students;
--重命名表
rename table 旧表名 to 新表名;
rename table students to stu;
'''3.3.4-表数据增删改查'''
--查看所有列
select * from 表名;
select * from student;
--查询指定列
select column1,column2,column3 from 表名;
select id,name from student;
--查询，使用as给表起别名
select 字段名 from 表名 as 新表名;
select name from student as s;--给表起别名
select name as n from student;--给列起别名
--消除重复行
select distinct column1，... from 表名;
select distinct name from student;
--增加
insert into 表名 values(...);
insert into student values(null,"郭靖","襄阳城","男");--此处第一个为自增长列，用null代替
--部分列插入，值的书序与给出的列对应
insert into 表名(column1,...) values(value1,...);
insert into student(name,address,gender) values("风清扬","后山洞","男");
--多行插入
insert into 表名(cloumn1,...) values(...),(...),...;
insert into student(name,address,gender) values("萧峰","丐帮","男"),("萧远山","大辽","男"),("小龙女","活死人墓","女");
--修改
update 表名 set column1=values1,column2=values2... where 条件
update student set name="黄蓉",gender="女" where name="萧远山"
--删除
delete from table_name where 条件;
delete from student where id=5;
--逻辑删除,本质上为更新
update table_name set isdelete = 0;
--清空数据（会把权标都清空，且自增长键为1）
truncate table_name;

'''3.3数据库备份与恢复'''
mysqldump -uroot -p 数据库名 >shuju.sql--数据库备份
--连接mysql，创建新的数据库，准备恢复数据
--退出mysql链接，执行下面命令
mysql -uroot -p 新数据库名<shuju.sql

'''3.4条件查询'''
--查询编号大于3的学生信息
select * from student where id>3;
--查询姓名不是“小明”的学生信息
select * from student where name!="小明";
--查询编号大于3的女生
select * from student where id>3 and gender="女";
--模糊查询，查询姓刘的学生
select * from student where name like "刘%";
--查询姓刘切名字为两个字的学生信息
select * from student where name like "刘_";
--范围查询
select * from student where id in(1,3,8);
--查询编号为1-8的学生信息
select * from student where id between 1 and 8;
--查询编号为3-6的男生信息
select * from student where (id between 3 and 6) and gender="男";
--空判断。注意null与""是不相同的，查询没有填写身高的学生
select * from students where height is null;
--查询填写了身高的男生信息
select * from students where height is not null and gender="男";

'''3.5排序'''
--查询男生信息，按照ID降序排列
select * from student order by id desc;
--显示所有的学生信息，先按照年龄从大--》小排序,当年龄相同时按照身高降序
select * from student order by age desc,height desc;

'''3.6聚合函数'''
--查询学生总数，使用count(*)
select count(*) from student;
--查询女生的编号最大值
select max(id) from student where gender="女";
--查询男生的编号最小值
select min(id) from student where gender="男";
--查询男生的总年龄
select sum(age) from student where gender="男";
--查询女生的平均年龄
select avg(age) from student where gender="女";
--四舍五入，查询女生的平均年龄并保存两位小数
select round(avg(age),2) from student where gender="女";

'''4、高级查询'''
'''4.1-分组-group by'''
--根据性别分组
select gender from student group by gender;
--group by + group_concat(),根据分组结果使用group_concat()放置每一组的某字段的值集合
select gender,group_concat(name) from student group by gender;
--使用group_concat()和group by显示相同名字的人的id号
'''4.2-group by +group_concat()'''
select name,group_concat(id) from student group by name;
'''结果如下：
name	group_concat(id)
哪吒	1
小龙女	6,9
萧峰	4,7
萧远山	8
郭靖	2
风清扬	3
黄蓉	5
'''
--基于上面例子按照id排序，并且设置分隔符为_
select name,group_concat(id order by id desc separator '_') as '合集' from student group by name;
'''结果如下：
name	合集
哪吒	1
小龙女	9_6
萧峰	7_4
萧远山	8
郭靖	2
风清扬	3
黄蓉	5
'''
'''####函数介绍###
1、concat():用于连接两个或多个数组。该方法不会改变现有的数组，而仅仅会返回被连接数组的一个副本。
2、concat_ws():和concat()一样，将多个字符串连接成一个字符串，但是可以一次性指定分隔符～（concat_ws就是concat with separator）
	语法：concat_ws(separator, str1, str2, ...)
3、group_concat需要配合group by使用才能达到效果
'''
'''4.3-group by +聚合函数'''
--统计不同性别的人的平均年龄
select gender,avg(age) from student group by gender;
--统计不同性别的人的个数
select gender count(*) from student group by gender;

'''4.4 group by +having '''
--查询不同性别人的数量，输出数量大于2的性别
select gender,count(*) from student group by gender haing count(*)>2
'''4.5 group by + with roll up'''
--with rollup 的作用是在最后新增一行，来记录当前列里所有记录的和
select gender,count(*) from student group by gender with rollup;
'''结果如下：
gender	count(*)
女		3
男		6
		9 
最后一行的 9，是累加的值
'''

'''4.4、分页'''
--select * from 表名 limit start,count;
--查询前三行男生信息
select * from student where gender="男" limit 0,3;
--查询第N页的数据
select * from student where id>3 limit (n-1)*m,m;

'''5、链接查询'''
'''5.1 内连接查询'''
--内连接查询:查询的结果为两个表匹配到的数据，即两个表的公共数据
--查询班级表与学生表
selct * from student inner join classes on students.cls_id=classes.id;
--查询学生姓名及班级姓名
select s.name,c.name from student as s inner join classes as c on s.cls_id=c.id;

'''5.2 左连接查询'''
--查询的结果为两个表匹配到的数据，对于右表中不存在的值用null来填充
select * from student as s left join classes as c on s.cls_id=c.id;

'''5.3 右连接查询'''
--查询的结果为两个表匹配到的数据，对于左表中不存在的值用null来填充
select * from student as s right join classes as c on s.cls_id=c.id;


'''FAQ'''
1、提示您在使用安全的update模式，只能通过主键对表进行修改
You are using safe update mode and you tried to update a table without a WHERE that uses a KEY column.
SET SQL_SAFE_UPDATES = 0;0 不启用；1 启用