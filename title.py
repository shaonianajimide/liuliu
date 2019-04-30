#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import threading
import queue
from bs4 import BeautifulSoup
import re
import time

zz=r'\<title\>.*?\</title\>'
q=queue.Queue()
title=[]
with open('ruourl.txt', 'r') as f:
    for i in f.readlines():
        i = i.strip()
        q.put(i)

print(q.qsize())

class mythread(threading.Thread):
    def __init__(self,q):
        threading.Thread.__init__(self)
        self.q = q
    def run(self):
        while self.q.empty() == False:
            try:
                url1 = self.q.get()
                url = 'http://' + url1
                res = requests.get(url)
                res.encoding = 'utf-8'
                html = BeautifulSoup(res.text, 'html.parser')
                title=str(html.select('title')[0].text)
                with open('ruokou.txt','a+') as file:
                    file.write(url+'-----'+title+'\n')
                    print(title)
            except:
                print('错误')
t1=[]
for i in range(50):
    t=mythread(q)
    t.start()
    t1.append(t)

for i in t1:
    i.join()

