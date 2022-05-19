from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev'
    )
    # Load environment variables with FLASK_ prefix
    app.config.from_prefixed_env()

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    # Main route and function
    @app.route('/api/v1/hello')
    def client_api():
        try:    
            if app.config['CLIENTNAME'] == 'CustomerA':
                return 'Hi'
            if app.config['CLIENTNAME'] == 'CustomerB':
                return 'Dear Sir or Madam'
            if app.config['CLIENTNAME'] == 'CustomerC':
                return 'Moin'
        except KeyError as e:
            return 'Please, setup FLASK_CLIENTNAME environment variable'
    
    return app