#!/usr/bin/env python3
import os
from http import cookies

cookie = cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
name = cookie.get("name")

print('<html><body>')
if name is None:
    # cookie['name'] = 'value'
    # cookie['counter'] = '100'
    print("Set-cookie: name=value")
    #print("Set-cookie: counter=0")
    print("Content-type: text/html\n")
    print('Cookie have been created!!!')
else:
    print("Content-type: text/html\n")
    print('Cookie are already created!')

print('<br><br>')
print(cookie)
print('</body></html>')

