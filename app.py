from flask import Flask, request, render_template, flash
from weather import weather
from give_png import give_png

app = Flask(__name__)
app.config['SECRET_KEY'] = '\xe8\xdd\xa8\xc2k\x0by\x12h=\xe6HW\xe7\x11\xb3\xaeO\x90\xbdV\xb0\xbd\xde'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('city') == "":
            flash('А ты не заполнил форму✌️')
            return render_template('index.html')
        city = request.form.get('city').title()
        data = weather(city)
        if not data:
            flash('Город не найден😔')
            return render_template('index.html')
        day_weather, week_weather = data
        print(day_weather)
        week_weather_list = list(week_weather.items())[0:2]
        return render_template('index.html',city=city, style='is-visible', temp_day=day_weather[0], png=give_png(day_weather[1]), week_weather=week_weather_list)

    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0')
