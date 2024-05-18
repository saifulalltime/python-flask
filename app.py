from flask import Flask

app = Flask(__name__)
app.secret_key = "dwhdiu2h2903e"

@app.route("/")
def index():
  return 'Hello World! sadfasdfasdfdas'

@app.route("/<string:name>")
def hello(name):
    return "Hello " + name

if __name__ == '__main__':
  app.run()