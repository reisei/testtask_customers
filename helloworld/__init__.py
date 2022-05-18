from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev'
    )

    if test_config is None:
        app.config.from_mapping(test_config)

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    @app.route('/api/v1/hello')
    def client_api():
        pass
    
    return app