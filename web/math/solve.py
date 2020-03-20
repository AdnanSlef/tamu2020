#!/usr/bin/env python3
import requests

url = 'http://mentalmath.tamuctf.com/ajax/new_problem'
while 1:
    myobj = {'problem':input('problem: '),'answer':input('answer: ')}
    res = requests.post(url,data=myobj)
    print(myobj)
    print(res.text)
    print(res.json()['correct'])
