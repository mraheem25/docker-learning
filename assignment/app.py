# app.py

from flask import Flask
import redis

app = Flask(__name__)
r = redis.Redis(host='redis' , port=6379)

@app.route('/')
def welcome_message():
    return 'Hello, thank you for visiting our page!'

@app.route('/count')
def visit_count():
    count = r.incr('visit')
    return f'Our page has been visited {count} times'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)