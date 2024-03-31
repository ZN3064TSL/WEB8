from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/index')
def workpiece():
    return render_template('base.html', title='Заготовка')


@app.route('/training/<prof>')
def training(prof):
    params = {
        'space_ship1': url_for('static', filename='space_ship1.jpeg'),
        'space_ship2': url_for('static', filename='space_ship2.jpeg'),
        'prof': prof
    }
    return render_template('training.html', **params)


@app.route('/list_prof/<list>')
def list_prof(list):
    profs = ['Инженер-исследователь',
             'Пилот',
             'Строитель',
             'Экзобиолог',
             'Врач',
             'Инженер по терраформированию',
             'Климатолог',
             'Специалист по радиационной защите',
             'Астрогеолог',
             'Гляциолог',
             'Инженер жизнеобеспечения',
             'Метеоролог',
             'Оператор марсохода',
             'Киберинженер',
             'Штурман',
             'Пилот дронов']
    return render_template('list_prof.html', list=list, profs=profs)

@app.route('/')
@app.route('/answer')
@app.route('/auto_answer')
def answer():
    form = {'title': 'Анкета',
            'surname': 'Watny',
            'name': 'Mark',
            'education': 'Выше среднего',
            'profession': 'Штурман марсохода',
            'sex': 'Male',
            'motivation': 'Всегда мечтал застрять на Марсе!',
            'ready': True}
    return render_template('answer.html', **form, css=url_for('static', filename='answer.css'))

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
