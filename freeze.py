from flask_frozen import Freezer
# Замініть 'app' на назву вашого головного файлу без .py
# А другий 'app' — на назву змінної додатка Flask всередині того файлу
from app import app 

# Налаштування для GitHub Pages (щоб посилання працювали коректно)
app.config['FREEZER_DESTINATION IGNORE'] = ['.git*']
app.config['FREEZER_RELATIVE_URLS'] = True

def pages():
    yield {'page': 'index'}
    yield {'page': 'about'}

freezer = Freezer(app)

if __name__ == '__main__':
    print("--- Процес заморозки розпочато ---")
    try:
        freezer.freeze()
        print("--- Готово! Шукайте файли в папці 'build' ---")
    except Exception as e:
        print(f"Помилка під час заморозки: {e}")
