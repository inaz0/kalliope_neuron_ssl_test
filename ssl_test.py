# -*- coding: utf-8 -*-
import re
import sys  
import datetime
import requests
import urllib.request as urllib_request

import time
import urllib

from time import sleep
from kalliope.core.NeuronModule import NeuronModule, MissingParameterException
from kalliope import Utils


class Ssl_test(NeuronModule):
    def __init__(self, **kwargs):
        super(Ssl_test, self).__init__(**kwargs)
        # Basic configuration
        self.query = kwargs.get('query', None)
        r = requests.get('https://www.ssllabs.com/ssltest/analyze.html?d=' + self.query + '&hideResults=on&latest=&clearCache=on')
        
        isFinish = False

        if r.status_code != 200:
            self.message = {
            "summary": "Le test est terminé",
            "returncode": 500
            }   
        else:
            while isFinish == False:
              time.sleep(0.4)
              isFinish = self.checkIfTestIsFinish()
            
            self.message = {
            "summary": "Le test est terminé",
            "returncode": 200
            }
            
            self.say(self.message)
        
    def checkIfTestIsFinish(self):

        r = requests.get('https://www.ssllabs.com/ssltest/analyze.html?d=' + self.query + '&hideResults=on&latest=')

        m = re.search('(\d*)%.complete', r.text)

        if m == None:
            print("finish")
            return True
        else:
            print(m.group(0))
            return False



