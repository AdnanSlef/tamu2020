#!/usr/bin/env python3
import requests

url = 'http://mentalmath.tamuctf.com/ajax/new_problem'
while 1:
    myobj = {input('problem: '):input('answer: ')}
    res = requests.post(url,data=myobj)
    print(res.text)
    print(res.json()['correct'])
