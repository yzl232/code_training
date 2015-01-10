# encoding=utf-8
'''
Design a mobile phone class. For example, iPhone is manufactured by Apple and the software iOS is also from Apple. Samsung GALAXY is produced by Samsung but the software is Android from Google. Also take into account the version of the software, ex., iOS 7.1, 8.0.
'''
class Phone:
    def __init__(self,  os, manufacturer):
        self.os = os
        self.manufacturer = manufacturer

class Company:
    def __init__(self, name):
        self.name = name

class OS:
    def __init__(self,  name,  version, manufacturer):
        self.name = name
        self.version = version
        self.manufacturer = manufacturer