#!/usr/bin/env python3

# This code is from the recorded and in-person labs

import cgi
import cgitb
cgitb.enable()

import os
from templates import login_page, secret_page, after_login_incorrect
import secret
from http.cookies import SimpleCookie

# parse cookies and create a dict of cookies
def parse_cookies(cookie_string):
    result = {}
    if cookie_string == "":
        return result
    
    cookies = cookie_string.split(";")
    for cookie in cookies:
        split_cookie = cookie.split("=")
        result[split_cookie[0]] = split_cookie[1]

    return result

cookies = parse_cookies(os.environ["HTTP_COOKIE"])

# set up cgi form
form = cgi.FieldStorage()
username = form.getfirst("username")
password = form.getfirst("password")

# assemble header and body
header = ""
header += "Content-Type: text/html\r\n"

body = ""

# if user is not logged in, show login page
# if user enters correct username and password, show secret page
# else show login incorrect page
if not username and not password:
    body += login_page()
elif username == secret.username and password == secret.password:
    body += secret_page(username, password)
    header += "Set-Cookie: logged=true; Max-Age60\r\n"
    header += "Set-Cookie: cookie=nom\r\n"
    body += "<h1>A terrible secret</h1>"
else:
    body += after_login_incorrect()

# print header and body
print(header)
print()
print(body)