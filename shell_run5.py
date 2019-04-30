import requests
from concurrent.futures import ThreadPoolExecutor
import sys
import urllib2
import re
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import os

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

host_r = re.compile(r'host=(.*?);')
url_r = re.compile(r'url=(?:https?\://[^/]+)?/+(.*?);')
pwd_r = re.compile(r';body0=(.*?);head1=')

def poc(data):
	try:
		host = re.findall(host_r,data)[0]
		url = re.findall(url_r,data)[0]
	except:
		pass

	
	if url != "":
		try:
			req = urllib2.Request('http://' + host + '/' + url)
			rep = urllib2.urlopen(req,timeout=2)
			
			
		except:
			try:
				req = urllib2.Request('https://' + host + '/' + url)
				rep = urllib2.urlopen(req,timeout=2)
			except:
				print data.strip() + '\t' +'---false---'
		
		finally:
			if rep != '':
				html = rep.read()
				if rep.code == 200 and '<input' in html and not ' src' in html:
					print data.strip() + '\t' +'---true---' 
				else:
					print data.strip() + '\t' +'---false---'
	else:
		pass
		


def exp(f_name):

	with open(f_name,'r+') as f:
		
		with ThreadPoolExecutor(200) as executor:
			for each in f:
				info = each.strip()
				executor.submit(poc,info)
		

						
			

if __name__ == "__main__":
	exp(sys.argv[1])

	
	
	
