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
    <title>ROT13</title>
</head>
<body>
    <h1><b>Enter some text to ROT13</b></h1>
"""

page_footer = """
</body>
</html>
"""

ALPHABET_LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
ALPHABET_UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

textToEncrypt = ""

def alphabet_position(letter):
    alphabet = ALPHABET_LOWERCASE if letter.islower() else ALPHABET_UPPERCASE
    return alphabet.index(letter)

def rotate_char(char, rotation):
    if not char.isalpha():
        return char

    alphabet = ALPHABET_LOWERCASE if char.islower() else ALPHABET_UPPERCASE
    new_pos = (alphabet_position(char) + rotation) % 26
    return alphabet[new_pos]

def encrypt(text, rotation):
    answer = ""
    for char in text:
        answer += rotate_char(char, rotation)
    return answer

class MainHandler(webapp2.RequestHandler):
    def get(self):

        rotNumber = 0

        main_content = """
        <form action="/">
            <label>Enter text to encrypt</label>
            <input name="text-rot" value="%(textToEncrypt)s"><br>
            <label>Enter a number to rotate by</label>
            <input name="num-rot"><br>
            <input type=submit>
        </form>
        """

        textToEncrypt = self.request.get("text-rot")
        rotNumber = self.request.get("num-rot")
        textToEncrypt = encrypt(textToEncrypt, int(rotNumber))

        response = page_header + main_content + page_footer
        self.response.write(response)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
