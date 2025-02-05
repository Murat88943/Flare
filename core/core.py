import os
import subprocess
from flask import Flask, request, jsonify
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

    def build_apk(self, app_path):
        os.makedirs('build', exist_ok=True)
        command = f'buildozer -v android debug'
        process = subprocess.Popen(command, shell=True, cwd=app_path)
        process.wait()
        if process.returncode == 0:
            print("APK создан успешно!")
        else:
            print("Ошибка при создании APK.")


# Пример использования
if __name__ == "__main__":
    framework = MyFramework()


    @framework.route("/api/resource")
    def resource():
        return jsonify({"message": "Hello, World!"})


    framework.run(debug=True)

    # Команда для сборки APK из командной строки
    # framework.build_apk('/path/to/your/app')

