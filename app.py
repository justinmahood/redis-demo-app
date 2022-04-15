import logging
import os

import redis
from flask import Flask, render_template, request

redisHost = os.getenv('REDISHOST')

app = Flask(__name__)

# Change the format of messages logged to Stackdriver
logging.basicConfig(format='%(message)s', level=logging.INFO)

r = redis.Redis(host=redisHost, db=0)

class Info:  # Empty class as a handy object to store stuff in
    pass


@app.route('/')
def index():
    info = Info()
    try:
        info.lastBrowser = r.get("browser").decode("utf-8").title()
    except:
        info.lastBrowser = "No browser detected"
    
    try:
        info.lastVersion = r.get("version").decode("utf-8")
    except:
        info.lastVersion = "No version detected"

    info.currentBrowser = request.user_agent.browser.title()
    info.currentVersion = request.user_agent.version

    storeUserAgentValuesInRedis(request.user_agent)
    return render_template('index.html', info=info)


def storeUserAgentValuesInRedis(user_agent):
    r.set("browser", user_agent.browser)
    r.set("version", user_agent.version)
    return


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
