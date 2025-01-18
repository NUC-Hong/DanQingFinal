# coding=utf-8

from tornado.httpserver import HTTPServer
from tornado.wsgi import WSGIContainer
from app import app
from tornado.ioloop import IOLoop

s = HTTPServer(WSGIContainer(app))
s.listen(8000)  # 监听8000 端口
IOLoop.current().start()