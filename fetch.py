import re
from selenium import webdriver
import time

class fetch():
    def __init__(self):
        self.driver = webdriver.Chrome("./chromedriver")
        self.driver.implicitly_wait(10)
        self.bus = ''
        self.dest = ''
        self.time = ''
        self.status = ''
        
    def getbus(self):
        return self.bus
    
    def getdest(self):
        return self.dest
    
    def gettime(self):
        return self.time

    def getstatus(self):
        return self.status
    
    def set(self, bus):
        self.bus = bus
        self.driver.get("https://ebus.gov.taipei/VirtualStop/1156800620")
        html = self.driver.page_source
        

        pattern = f'<p class="auto-list-routelist-bus">{self.bus}.*?<\/a>'
        
        match = re.search(pattern, html, re.S)
        section = match.group(0)

        pattern_place = '<img.*?>(.*?)<\/p>'
        match_place = re.search(pattern_place, section, re.S)

        if (match_place != None):
            self.dest = match_place.group(1).replace('\n','').replace(' ','')

        pattern_time = '<span.*?time-in.*?>(.*?)<\/span>'
        match_time = re.search(pattern_time, section, re.S)
        if (match_time != None):
            self.time = match_time.group(1)

        else:
            self.time = ''

        pattern_status = '<span.*?position-none.*?>(.*?)<\/span>'

        match_status = re.search(pattern_status, section, re.S)
        if (match_status != None):
            self.status = match_status.group(1)

        pattern_status = '<span.*?position-now.*?>(.*?)<\/span>'

        match_status = re.search(pattern_status, section, re.S)
        if (match_status != None):
            self.status = match_status.group(1)

        if (not self.status):
            self.status = 'Normal'

        print('------------------------')
        print('bus: ' + str(self.bus))
        print('dest: ' + str(self.dest))
        print('estimated: ' + str(self.time))
        print('status: ' + str(self.status))

    def getMessage(self):
        message = str(self.bus) +'(' + str(self.dest) + ')\n'
        if (str(self.status) == 'Normal'):
            message = message + '約' + str(self.time) + '分鐘進站'
        if (str(self.status) == 'No Service'):
            message = message + '本日停駛'
        if (str(self.status) == 'Over Service'):
            message = message + '本日服務已結束,不再發車'
        if (str(self.status) == 'Coming Soon'):
            message = message + '即將進站'
        return message

 
