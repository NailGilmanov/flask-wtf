from flask import Flask, render_template
from data import db_session

from data.users import User


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


@app.route('/answer')
@app.route('/auto_answer')
def auto_answer():
    param = {}
    param['title'] = "first"
    param['surname'] = 'Watny'
    param['name'] = 'Mark'
    param['education'] = 'выше среднего'
    param['profession'] = 'штурман марсохода'
    param['sex'] = 'male'
    param['motivation'] = 'Всегда мечтал застрять на Марсе!'
    param['ready'] = 'True'
    return render_template('auto_answer.html', **param)


def main():
    db_session.global_init("db/mars_explorer.db")
    user1 = User()
    user1.name = 'Ridley'
    user1.surname = "Scott"
    user1.age = 21
    user1.position = 'captain'
    user1.speciality = 'research engineer'
    user1.address = 'module_1'
    user1.email = 'scott_chief@mars.org'

    user2 = User()
    user2.name = 'Mike'
    user2.surname = "Miller"
    user2.age = 35
    user2.position = 'trainee'
    user2.speciality = 'engineer'
    user2.address = 'module_2'
    user2.email = 'mike_miller@mars.org'

    user3 = User()
    user3.name = 'Johnny'
    user3.surname = "Jouster"
    user3.age = 25
    user3.position = 'trainee'
    user3.speciality = 'pilot'
    user3.address = 'module_1'
    user3.email = 'jojo@mars.org'

    user4 = User()
    user4.name = 'Giordano'
    user4.surname = "Giovanna"
    user4.age = 20
    user4.position = 'trainee'
    user4.speciality = 'pilot'
    user4.address = 'module_3'
    user4.email = 'golden_wind@mars.org'

    db_sess = db_session.create_session()
    db_sess.add(user1)
    db_sess.add(user2)
    db_sess.add(user3)
    db_sess.add(user4)
    db_sess.commit()
    # app.run()


if __name__ == '__main__':
    main()
