# -*- coding: utf-8 -*-
import re
import sys  
import datetime
import requests
import urllib.request as urllib_request

import urllib

from time import sleep
from kalliope.core.NeuronModule import NeuronModule, MissingParameterException
from kalliope import Utils


class Ssl_test(NeuronModule):
    def __init__(self, **kwargs):
        super(Ssl_test, self).__init__(**kwargs)
        # Basic configuration
        self.query = kwargs.get('query', None)
        r = requests.get('https://www.ssllabs.com/ssltest/analyze.html?d=' + self.query + '&hideResults=on&latest=')
		
        self.returnCode = r.status_code
		
        self.message = {
        "summary": "Le test est lancé !",
        "returncode": self.returnCode
        }

        self.say(self.message)
		
		m = re.search('Please wait..', r.text)
		
		self.message = {
        "summary": m.group(0),
        "returncode": self.returnCode
        }