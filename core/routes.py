from flask import Flask
from jinja2 import Environment, FileSystemLoader


class MyFramework:
    def __init__(self, template_folder='templates'):
        self.app = Flask(__name__)
        self.template_env = Environment(loader=FileSystemLoader(template_folder))

    def route(self, path):
        def wrapper(func):
            self.app.add_url_rule(path, view_func=func)
            return func

        return wrapper

    def render(self, template_name, **context):
        template = self.template_env.get_template(template_name)
        return template.render(context)

    def run(self, host='127.0.0.1', port=5000):
        self.app.run(host=host, port=port)


class Router:
    def __init__(self, framework):
        self.framework = framework

    def add_route(self, path, view_func):
        self.framework.route(path)(view_func)


