'''
    留言板-错误处理
'''
from flask import render_template
from app import app

@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404