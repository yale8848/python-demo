#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import Student

def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

def add(x, y, f):
    return f(x) + f(y)


s = Student.Student()
s.score = 60

#print(json.dumps(s.__dict__))


def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

#c = consumer()
#produce(c)

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
bicycles.append('aaa')
bicycles.insert(2,'cc')
del bicycles[2]
bicycles.sort(reverse=True)
for b in bicycles:
    if b == 'aaa':
        print(b)
    else:
        print('0---')
    print(b)

print(bicycles)


user_0 = {
'username': 'efermi',
'first': 'enrico',
'last': 'fermi',
}

for k,v in user_0.items():
    print(k+" "+v)

list = ["aa"]

def modify_list(list):
    list[0]='bb'
modify_list(list)
print(list)


def user_info(name,age,**infos):
    info={}
    info['name']=name
    info['age']=age
    for k,v in infos.items():
        info[k]=v
    return info

print(user_info('aaa',11,home='xian',hobby='play'))