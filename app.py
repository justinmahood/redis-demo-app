import os
import logging
import redis

from flask import Flask, render_template

# Change the format of messages logged to Stackdriver
logging.basicConfig(format='%(message)s', level=logging.INFO)

app = Flask(__name__)
redisHost = os.getenv('redis_host')
print(redisHost)
redisPassword = os.getenv('redis_password')


@app.route('/')
def index():
    return render_template('index.html', val=getRedisValue('foo'))


def getRedisValue(keyname):
    r = redis.Redis(host=redisHost, db=0, password=redisPassword)
    return r.get(keyname)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
