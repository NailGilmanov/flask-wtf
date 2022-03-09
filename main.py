from flask import Flask, render_template


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/index/<string:title>')
def index1(title):
    return render_template('base.html', title=title)


def main():
    app.run()


if __name__ == '__main__':
    main()
