# -*- coding: utf-8 -*-


class Human:
    def sai_hi(self):
        print(self.name, 'says', self.hi)

class American(Human):
    hi = 'Hello'
    def __init__(self, name):
        self.name = name
        self.hi = 'Hello'

class French(Human):
    hi = 'Hello'
    
    def __init__(self, name):
        self.name = name
        self.hi = 'Bonjour'

class Spanish(Human):
    hi = 'Hello'
    
    def __init__(self, name):
        self.name = name
        self.hi = 'Hola'

class Janpanese(Human):
    hi = 'Hello'
    
    def __init__(self, name):
        self.name = name
        self.hi = 'Konnichiwa'

class Korean(Human):
    hi = 'Hello'
    
    def __init__(self, name):
        self.name = name
        self.hi = 'Yeoboseyo'


class Indian(Human):
    hi = 'Hello'
    
    def __init__(self, name):
        self.name = name
        self.hi = 'Namaste'