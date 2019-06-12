#coding:utf-8
from selenium import webdriver
import re
import sys
import datetime
import os
import requests
import time
from PIL import Image
from PIL import ImageGrab
import webbrowser
import win32api
import win32con
from bs4 import BeautifulSoup 

ticks=datetime.date.today() + datetime.timedelta(-1)
tick=datetime.date.today() + datetime.timedelta(-2)
rew=r'(.*?)/'
title=r'<title>(.*?)</title>'
s=str(ticks)+'yijiazu'
z=str(ticks)+'zhongdian'
wj=s+'.txt'
wz=z+'.txt'
a=1
b=1
zxc=1
cxz=1
try:
	os.mkdir(s)
	os.mkdir(z)
except:
	print "已创建"
with open(wj,'r+') as f:
	for i in f:
		try:
			url='http://'+i.strip()
			webbrowser.open(url)
			d=str("%04d" % a)+'_'+i.strip().replace(':','-')+'_'+s
			time.sleep(4)
			#img=ImageGrab.grab()
			im = ImageGrab.grabclipboard()
			while True:
				win32api.keybd_event(win32con.VK_SNAPSHOT, 0, 0, 0)
				time.sleep(1)
				win32api.keybd_event(win32con.VK_SNAPSHOT, 0, win32con.KEYEVENTF_KEYUP, 0)
				filename = s+'/'+d.replace('/','-')+'.png'
				im = ImageGrab.grabclipboard()
				if im is None:
					print('===>is None ')
				else:
					print('===>' + str(im.size))
					break
			im = im.crop()
			im.show()
			im.save(filename, 'PNG')
			a=a+1
			os.system('taskkill /im chrome.exe /f')
			time.sleep(2)
			os.system('taskkill /im Microsoft.Photos.exe /f')
		except:
			a=a+1

with open(wz,'r+') as f:
	for i in f:
		try:
			url='http://'+i.strip()
			webbrowser.open(url)
			d=str("%04d" % b)+'_'+i.strip().replace(':','-')+'_'+z
			time.sleep(4)
			im = ImageGrab.grabclipboard()
			while True:
				win32api.keybd_event(win32con.VK_SNAPSHOT, 0, 0, 0)
				time.sleep(1)
				win32api.keybd_event(win32con.VK_SNAPSHOT, 0, win32con.KEYEVENTF_KEYUP, 0)
				filename = z+'/'+d.replace('/','-')+'.png'
				im = ImageGrab.grabclipboard()
				if im is None:
					print('===>is None ')
				else:
					print('===>' + str(im.size))
					break
			im = im.crop()
			im.show()
			im.save(filename, 'PNG')
			b=b+1
			os.system('taskkill /im chrome.exe /f')
			time.sleep(2)
			os.system('taskkill /im Microsoft.Photos.exe /f')
		except:
			b=b+1			
			
with open(wj,'r+') as fi:
	for i in fi:
		try:
			ddd=str("%04d" % zxc)+'_'+i.strip().replace(':','-')+'_'+s
			filename = s+'/'+ddd.replace('/','-')+'.png'
			url2=re.findall(rew,i)[0]
			urls='http://'+url2
			res=requests.get(urls)
			html=BeautifulSoup(res.text,'html.parser')
			title2=re.findall(title,str(html))[0]
			v=str(ticks)+'yijiazutime.txt'
			with open(v,'r+') as f:
				for t in f:
					if url2 in t:
						time=t
						break
			d=s+'/'+s+'.csv'
			with open(d,'a+') as fil:
				fil.write(str("%04d" % zxc)+'\t'+url2+'\t'+title2+'\t'+time.strip()+'\t'+filename+'\n')
			zxc=zxc+1
		except:
			ddd=str("%04d" % zxc)+'_'+i.strip().replace(':','-')+'_'+s
			filename = s+'/'+ddd.replace('/','-')+'.png'
			url2=re.findall(rew,i)[0]
			v=str(ticks)+'yijiazutime.txt'
			with open(v,'r+') as f:
				for t in f:
					if url2 in t:
						time=t
						break
			d=s+'/'+s+'.csv'
			with open(d,'a+') as fil:
				fil.write(str("%04d" % zxc)+'\t'+url2+'\t'+'没有获取到title'+'\t'+time.strip()+'\t'+filename+'\n')
			zxc=zxc+1

with open(wz,'r+') as fi:
	for i in fi:
		try:
			ddd=str("%04d" % cxz)+'_'+i.strip().replace(':','-')+'_'+z
			filename = z+'/'+ddd.replace('/','-')+'.png'
			url2=re.findall(rew,i)[0]
			urls='http://'+url2
			res=requests.get(urls)
			html=BeautifulSoup(res.text,'html.parser')
			title2=re.findall(title,str(html))[0]
			s=str(ticks)+'zhongdiantime.txt'
			with open(s,'r+') as f:
				for t in f:
					if url2 in t:
						time=t
						break
			d=z+'/'+z+'.csv'
			with open(d,'a+') as fil:
				fil.write(str("%04d" % cxz)+'\t'+url2+'\t'+title2+'\t'+time.strip()+'\t'+filename+'\n')
			cxz=cxz+1
		except:
			ddd=str("%04d" % cxz)+'_'+i.strip().replace(':','-')+'_'+z
			filename = z+'/'+ddd.replace('/','-')+'.png'
			url2=re.findall(rew,i)[0]
			s=str(ticks)+'zhongdiantime.txt'
			with open(s,'r+') as f:
				for t in f:
					if url2 in t:
						time=t
						break
			d=z+'/'+z+'.csv'
			with open(d,'a+') as fil:
				fil.write(str("%04d" % cxz)+'\t'+url2+'\t'+'没有获取到title'+'\t'+time.strip()+'\t'+filename+'\n')
			cxz=cxz+1
dlyijiazu='del '+str(tick)+'yijiazutime.txt'
dlyijiazutime='del '+str(tick)+'yijiazu.txt'
dlzhongdian='del '+str(tick)+'zhongdian.txt'
dlzhongdiantime='del '+str(tick)+'zhongdiantime.txt'
os.system(dlyijiazu)
os.system(dlyijiazutime)
os.system(dlzhongdian)
os.system(dlzhongdiantime)