#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import re
import cgi

page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>User Signup</title>
    <style type="text/css">
      .label {text-align: right}
      .error {color: red}
    </style>

</head>
<body>
    <h1>
        <a href="/">Signup</a>
    </h1>
</body>
</html>
"""


signup_form = """
<form method="post">
    <table>
        <tbody>
            <tr>
                <td>
                    <label for="username">Username</label>
                </td>
                <td>
                    <input name="username" type="text" value="%(username)s">
                    <span class="error">%(username_error)s</span>
                </td>
            </tr>
            <tr>
                <td>
                    <label for="password">Password</label>
                </td>
                <td>
                    <input name="password" type="password">
                    <span class="error">%(password_error)s</span>
                </td>
            </tr>
            <tr>
                <td>
                    <label for="verify">Verify Password</label>
                </td>
                <td>
                    <input name="verify" type="password">
                    <span class="error">%(verify_error)s</span>
                </td>
            </tr>
            <tr>
                <td>
                    <label for="email">Email (optional)</label>
                </td>
                <td>
                    <input name="email" type="email" value="%(email)s">
                    <span class="error">%(email_error)s</span>
                </td>
            </tr>
        </tbody>
    </table>
    <input type="submit">
</form>
"""
content = page_header + signup_form


USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return username and USER_RE.match(username)

PASS_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
    return password and PASS_RE.match(password)

EMAIL_RE  = re.compile(r'^[\S]+@[\S]+\.[\S]+$')
def valid_email(email):
    return not email or EMAIL_RE.match(email)

def escape_html(s):
    return cgi.escape(s, quote=True)


class MainPage(webapp2.RequestHandler):

    def write_form(self, username="", email="", username_error="", password_error="",
                   verify_error="", email_error=""):
        self.response.out.write(content % {"username": escape_html(username),
                                           "email": escape_html(email),
                                           "username_error": escape_html(username_error),
                                           "password_error": escape_html(password_error),
                                           "verify_error": escape_html(verify_error),
                                           "email_error": escape_html(email_error)})

    def get(self):
        self.write_form()


    def post(self):
        have_error = False
        username = self.request.get('username')
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email')

        params = dict(username = username,
                      email = email)

        if not valid_username(username):
            params['username_error'] = "That's not a valid username."
            have_error = True

        if not valid_password(password):
            params['password_error'] = "That wasn't a valid password."
            have_error = True
        elif password != verify:
            params['verify_error'] = "Your passwords didn't match."
            have_error = True

        if not valid_email(email):
            params['email_error'] = "That's not a valid email."
            have_error = True

        if have_error:
            self.write_form(**params)
            
        else:
            self.redirect('/welcome?username=' + username)

class AddUser(webapp2.RequestHandler):

    def get(self):
        username = self.request.get('username')
        welcome = "<h1> Welcome, " + username + "!</h1>"
        self.response.out.write(welcome)



app = webapp2.WSGIApplication([('/', MainPage), ('/welcome', AddUser)],
                             debug=True)
