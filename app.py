import os
import logging
import redis

from flask import Flask

# Change the format of messages logged to Stackdriver
logging.basicConfig(format='%(message)s', level=logging.INFO)

app = Flask(__name__)
redisHost = os.getenv('redis_host')
redisPassword = os.getenv('redis_password')


@app.route('/')
def home():
    val = getRedisValue('foo')
    html = """
<html>
 <head>
  <title>
   Google Cloud Run - Sample Python Flask Example
  </title>
 </head>
 <body>
  <p>Hello Google Cloud Run World!</p> <p>THE VALUE OF FOO IS """
    html += str(val)
    html += """ </p>
  <a href="https://cloud.google.com/run/" target="_blank">Google Cloud Run Website</a>
 </body>
</html>
"""
    return html


def getRedisValue(keyname):
    r = redis.Redis(host=redisHost, db=0, password=redisPassword)
    return r.get(keyname)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
