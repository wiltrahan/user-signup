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

page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>User Signup</title>
</head>
<body>
    <h1>Signup</h1>
</body>
</html>
"""

class Signup(webapp2.RequestHandler):

    def get(self):
        signup_form = """
        <form method="post">
            <table>
                <tbody>
                    <tr>
                        <td>
                            <label for="username">Username</label>
                        </td>
                        <td>
                            <input name="username" type="text" value required>
                            <span class="error"></span>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <label for="password">Password</label>
                        </td>
                        <td>
                            <input name="password" type="password" value required>
                            <span class="error"></span>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <label for="verify">Verify Password</label>
                        </td>
                        <td>
                            <input name="verify" type="password" value required>
                            <span class="error"></span>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <label for="email">Email (optional)</label>
                        </td>
                        <td>
                            <input name="email" type="email" value required>
                            <span class="error"></span>
                        </td>
                    </tr>
                </tbody>
            </table>
            <input type="submit">
        </form>
        """
        self.response.write(page_header + signup_form)
# class MainHandler(webapp2.RequestHandler):
#     def get(self):
#         self.response.write(page_header)

app = webapp2.WSGIApplication([
    ('/', Signup)
], debug=True)
