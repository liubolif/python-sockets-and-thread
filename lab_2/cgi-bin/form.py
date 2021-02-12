#!/usr/bin/env python3
import cgi
import html
import os
from http import cookies

form = cgi.FieldStorage()

# зчитуємо значення із текствоих полів
text1 = form.getfirst("name", "not specified")
text2 = form.getfirst("address", "not specified")
# проводимо екранування на випадок використання спецсимволів у вводі
text1 = html.escape(text1)
text2 = html.escape(text2)

# якщо вибрані інгредієнти
if form.getvalue('ingredient'):
    # то зчитуємо їх, і перетворюємо отриманий масив на рядок
    ingredients = form.getvalue('ingredient')
    if type(ingredients) == list and len(ingredients) != 1:
        ingredients = ', '.join(ingredients)
else:  # якщо не вибраний жодний інгредієнт - присвоюємо відповідне значення
    ingredients = "not specified"

# якщо вибраний розмір піци
if form.getvalue('size'):
    # то зчитуємо інформацію
    size = form.getvalue('size')
else:
    size = "not specified"



# інкрементуємо змінну кукі 'counter', що підраховує кількість заповнених користувачем форм
cookie = cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
# якщо такої змінної ще не було оголошено - ініціалізуємо її
if cookie.get("counter") is None:
    cookie['counter'] = '1'
    print(cookie)
else: # в іншому випадку збільшуємо на одиницю
    cookie['counter'] = str(1 + int(cookie['counter'].value))
    print(cookie)
counter = cookie['counter'].value



print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Processing form's data</title>
        </head>
        <body>""")

print("<h3>Your order of pizza is confirmed!</h3>")
print("<p><b>Your name:</b> <i>{}</i></p>".format(text1))
print("<p><b>Your delivery address:</b> <i>{}</i></p>".format(text2))
print("<p><b>Pizza ingredients:</b> <i>{}</i></p>".format(ingredients))
print("<p><b>Pizza size:</b> <i>{}</i></p>".format(size))
print("<br><p><u><b>Total count of submitted forms:</b> {}</u></p>".format(counter))
print("""</body>
        </html>""")
