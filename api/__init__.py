from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@127.0.0.1/flasktest'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route('/healthcheck')
def health_database_status():
    is_database_working = True
    output = 'database is ok'

    try:
        db.session.execute('SELECT 1')
    except Exception as e:
        output = str(e)
        is_database_working = False

    if is_database_working:
        return 'database is ok'
    else:
        return output


@app.route('/')
def hello_world():
    return 'Hello World!'
