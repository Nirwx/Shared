from flask import Flask
from metro import d, url_link_dict, test_response

app = Flask(__name__)

@app.route('/')
def index():
    return 'blah'


@app.route('/metro')
def metro():
    return url_link_dict(d)

if __name__ == "__main__":
    app.run('127.0.0.1:8000', debug=True)