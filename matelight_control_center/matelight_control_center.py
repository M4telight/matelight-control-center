from flask import Flask, render_template, request

from matelight_connector import MatelightConnector

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def main():
    return render_template('home.html')


@app.route('/show-color-picker')
def show_color_picker():
    return render_template('color_picker.html')


@app.route('/set-color', methods=['POST'])
def set_color():
    color = request.form['color']
    connector.show_color(color)
    return '', 204


@app.route('/stop', methods=['GET'])
def stop():
    connector.stop()
    return '', 204


if __name__ == "__main__":
    connector = MatelightConnector()
    app.run(use_reloader=True)
    # app.run()