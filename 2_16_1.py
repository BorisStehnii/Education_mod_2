'''
Create a class method named `validate`, which should be called from the `__init__` method to validate parameter email,
passed to the constructor.
The logic inside the `validate` method could be to check if the passed email parameter is a valid email string.
'''

import re


class Validate():

    def __init__(self, email_string):
        if self.validate(email_string):
            self._email_string = email_string
            print(f"{email_string} address accepted")
        else:
            msg = f"{email_string} NOT email"
            print(msg)

    def validate(self, string_):
        if isinstance(string_, str) and re.findall(r'^\w+[.-]?\w+[.-]?\w+[@]\w+[.-]?\w+[.-]?\w+$', string_):
            answer = True
        else:
            answer = False
        return answer


Validate("true@mail.com")
Validate("tru-e@mail.com")
Validate("tru.e@mail.com")
Validate("tr@u_e@ma-il.com")
Validate("false>@mail.com")
Validate("fals..e@mail.com")
Validate("fa#lse@mail.com")
Validate("false @mail.com")
Validate("false@ma#il.com")
