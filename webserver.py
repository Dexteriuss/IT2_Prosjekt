from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>IT2-Prosjekt</h1>'
    return '<img>http://www.naturephoto-cz.com/fullsize/others/green-tree-python-47592.jpg</img>'

app.run()