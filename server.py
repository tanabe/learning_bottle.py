from bottle import route, run, template, static_file
import os

@route('/')
@route('/hello/<name>')
def hello(name='world'):
    return template('hello_template')

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root=os.getcwd() + '/static')

print os.getcwd()

run(host='localhost', port=8080, reloader=True)
