# Імпорт Flask для створення веб-додатку
from flask import Flask, render_template

# Створюємо додаток Flask
app = Flask(__name__)

# Маршрут для головної сторінки
@app.route('/')
def home():
    # Повертаємо шаблон index.html
    return render_template('index.html')

# Маршрут для сторінки "Про нас"
@app.route('/about')
def about():
    # Повертаємо шаблон about.html
    return render_template('about.html')

# Маршрут для сторінки контактів
@app.route('/contacts')
def contacts():
    # Повертаємо шаблон contacts.html
    return render_template('contacts.html')

@app.route('/mods')
def mods():
    # Повертаємо шаблон mods.html
    return render_template('mods.html')

# Якщо файл запущений безпосередньо, запускаємо сервер
if __name__ == '__main__':
    # Запускаємо додаток у режимі debug для розробки
    app.run(debug=True)