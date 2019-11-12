import os
from flask import Flask
from metro import MetroApiOperations

MetroApiOperations = MetroApiOperations()

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def index():
        return 'Healthy'    \

    @app.route('/query', methods=('GET', 'POST'))
    def search():
        test = '''[
  {
    \"columns\":[
      {\"text\":\"Time\",\"type\":\"time\"},
      {\"text\":\"Country\",\"type\":\"string\"},
      {\"text\":\"Number\",\"type\":\"number\"}
    ],
    \"rows\":[
      [1567084178599
      [1567081996000,\"SE\",123],
      [1567080915000,\"DE\",231],
      [1567080015000,\"US\",321]
    ],
    \"type\":\"table\"
  }
]'''
        return test

    @app.route('/metro')
    def metro():

        return MetroApiOperations.test_response()


    return app

if __name__ == '__main__':
    app = create_app()
    app.run('192.168.56.1')