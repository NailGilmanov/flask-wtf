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


@app.route('/list_prof/<string:type>')
def list_prof(type):
    profs = [
        "инженер-исследователь",
        "пилот",
        "строитель ",
        "экзобиолог",
        "врач",
        "инженер по терраформированию",
        "климатолог",
        "специалист по радиационной защите",
        "астрогеолог",
        "гляциолог",
        "инженер жизнеобеспечения",
        "метеоролог",
        "оператор марсохода",
        "киберинженер",
        "штурман",
        "пилот дронов"
    ]
    return render_template('list_prof.html',
                           type=type,
                           profs=profs)


def main():
    app.run()


if __name__ == '__main__':
    main()
