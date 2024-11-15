from flask import Flask, render_template
from datetime import date

app = Flask(__name__)

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

data = {
    'name': 'Максим Хмылов',
    'age': calculate_age(date(2010, 10, 28)),
    'games': (('https://pyfy-games.itch.io/the-core', 'the core'),),
    'profession': 'Программист',
    'place': 'Россия, Дмитров',
    'languages': (('Русский', 70),('Английский', 45),('Немецкий', 3)),
    'description': 'Это д/з по программированию, потому-что мы изучаем сайтики. А еще мне не хочеться что-то придумывать',
    'education': (
                     ('Английский','До уровня В2', 'Уже на протяжениии 6 лет я занимался Английским', 'КАЖДУЮ НЕДЕЛЮ'),
                     ('Программирование','До Марта 2025','Этот сайт - домашка по этому доп. занятию', 'ПРЯМО СЕЙЧАС УРОК'),
                     ('Школа','До 11 класса', 'Я хочу дойти до 11, меня все устраивает', 'БУДЕТ ЕЩЕ ДОЛГО')
                 ),
}

@app.route('/')
def index():
    return render_template('index.html',data=data)

if __name__ == '__main__':
    app.run(debug=True)