'''
    留言板-视图函数
'''
from app import app,db
from datetime import datetime
from flask import flash,url_for,redirect,render_template,request
from app.models import TbMessage
from app.forms import MessageForm
import uuid

@app.before_first_request
def init():
    pass
#主页
@app.route('/', methods=['GET','POST'])
def index():
    messages = TbMessage.query.order_by(TbMessage.timestamp.desc()).all()
    form = MessageForm()
    if form.validate_on_submit():
        message = TbMessage(id=uuid.uuid4().hex, title=form.title.data, body=form.body.data)
        db.session.add(message)
        db.session.commit()
        flash('消息已发布!!!')
        return redirect(url_for('index'))   #重定向index视图,获取最新数据
    return render_template('index.html', form=form, messages=messages)
#mb:messageboard留言板
@app.route('/mb',methods=['GET','POST'])
def mb():
    a = 4 / 0
    messages = TbMessage.query.order_by(TbMessage.timestamp.desc()).all()
    form = MessageForm()
    if form.validate_on_submit():
        message = TbMessage(id=uuid.uuid4().hex, title=form.title.data, body=form.body.data)
        db.session.add(message)
        db.session.commit()
        flash('消息已发布!!!')
        return redirect(url_for('mb'))   #重定向board视图,获取最新数据
    return render_template('message/board.html',form=form, messages=messages)