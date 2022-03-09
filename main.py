from flask import Flask, render_template


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/index/<string:title>')
def index1(title):
    return render_template('base.html', title=title)


@app.route('/training/<string:prof>')
def training(prof):
    engineer_profs = False
    if prof in ['инженер', 'строитель']:
        engineer_profs = True
    return render_template('training.html', engineer_profs=engineer_profs)


def main():
    app.run()


if __name__ == '__main__':
    main()
