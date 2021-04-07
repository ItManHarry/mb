from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_moment import Moment
#程序实例
app = Flask('app')
app.debug = True
#导入配置
app.config.from_pyfile('settings.py')
#创建Bootstrap实例
boostrap = Bootstrap(app)
#创建时间控件Moment实例
moment = Moment(app)
#删除Jinja2 语句后的第一个空行
app.jinja_env.trim_blocks=True
#删除Jinja2 语句所在行之前的空格和制表符(tabs)
app.jinja_env.lstrip_blocks=True
#数据库实例
db = SQLAlchemy(app)
#初始化数据库
from app.models import init_db
init_db()
#导入各个模块
from app import views,errors,commands