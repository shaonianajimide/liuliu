#-*- coding:utf-8 -*-
import re
import os
import urllib

a=0
bs=os.popen('awk -F\"\t\" \'{print $10}\' shuju.txt').readlines()
data=os.popen('awk -F\"\t\" \'{print $1}\' shuju.txt').readlines()
userip=os.popen('awk -F\"\t\" \'{print $3}\' shuju.txt').readlines()
userdizhi=os.popen('awk -F\"\t\" \'{print $5}\' shuju.txt').readlines()
url1=r'host=(.*?);url='
username7065=r'username=(.*?)&'
password7065=r'password=(.*?)&'
realname7065=r'real_name=(.*?)&'
tel7065=r'tel=(.*?)&'
qq7065=r'qq_num=(.*?)&'
email7065=r'email=(.*?)&'
username7066=r'loginname=(.*?)&'
password7066=r'password=(.*?)&'
tel7066=r'bocai_phone=(.*?);'
username7079=r'username=(.*?)&'
password7079=r'password=(.*?)&'
realname7079=r'bocai_name=(.*?);'
tel7079=r'bocai_phone=(.*?);'
qq7079=r'bocai_qq=(.*?);'
username7071=r'username=(.*?)&'
password7071=r'repassword=(.*?)&'
realname7071=r'bocai_name=(.*?);'
tel7071=r'bocai_phone=(.*?);'
username7088=r'loginname%3D(.*?)%26'
password7088=r'pwd%3D(.*?)%26'
realname7088=r'username%3D(.*?)%26'
tel7088=r'phone%3D([0-9]{11})%26'
qq7088=r'bocai_qq=(.*?)%26'
user7054=r'A=(.*?)&'
user6903=r'account=(.*?)&'
user7056=r'UserName=(.*?)&'
user7055=r'userName=(.*?);'
user7072=r'accountid=(.*?)&'
dailiname=r'bocai_daili_name=(.*?);'
dailitel=r'bocai_daili_phone=(.*?);'
dailiemail=r'bocai_daili_email=(.*?);'
dailiweixin=r'bocai_daili_weixin=(.*?);'
dailicard=r'bocai_daili_card=(.*?);'
admin7060=r'LoginName=(.*?)&'
admin7061=r'user=(.*?)&'
data01=r' 01:.*:.*\.0\t0000'
data02=r' 02:.*:.*\.0\t0000'
data03=r' 03:.*:.*\.0\t0000'
data04=r' 04:.*:.*\.0\t0000'
data05=r' 05:.*:.*\.0\t0000'
data06=r' 06:.*:.*\.0\t0000'
data07=r' 07:.*:.*\.0\t0000'
data08=r' 08:.*:.*\.0\t0000'
data09=r' 09:.*:.*\.0\t0000'
data10=r' 10:.*:.*\.0\t0000'
data11=r' 11:.*:.*\.0\t0000'
data12=r' 12:.*:.*\.0\t0000'
data13=r' 13:.*:.*\.0\t0000'
data14=r' 14:.*:.*\.0\t0000'
data15=r' 15:.*:.*\.0\t0000'
data16=r' 16:.*:.*\.0\t0000'
data17=r' 17:.*:.*\.0\t0000'
data18=r' 18:.*:.*\.0\t0000'
data19=r' 19:.*:.*\.0\t0000'
data20=r' 20:.*:.*\.0\t0000'
data21=r' 21:.*:.*\.0\t0000'
data22=r' 22:.*:.*\.0\t0000'
data23=r' 23:.*:.*\.0\t0000'
data24=r' 24:.*:.*\.0\t0000'
ddata1=0
ddata2=0
ddata3=0
ddata4=0
ddata5=0
ddata6=0
ddata7=0
ddata8=0
ddata9=0
ddata10=0
ddata11=0
ddata12=0
ddata13=0
ddata14=0
ddata15=0
ddata16=0
ddata17=0
ddata18=0
ddata19=0
ddata20=0
ddata21=0
ddata22=0
ddata23=0
ddata24=0
dddata1=0
dddata2=0
dddata3=0
dddata4=0
dddata5=0
dddata6=0
dddata7=0
dddata8=0
dddata9=0
dddata10=0
dddata11=0
dddata12=0
dddata13=0
dddata14=0
dddata15=0
dddata16=0
dddata17=0
dddata18=0
dddata19=0
dddata20=0
dddata21=0
dddata22=0
dddata23=0
dddata24=0
addata1=0
addata2=0
addata3=0
addata4=0
addata5=0
addata6=0
addata7=0
addata8=0
addata9=0
addata10=0
addata11=0
addata12=0
addata13=0
addata14=0
addata15=0
addata16=0
addata17=0
addata18=0
addata19=0
addata20=0
addata21=0
addata22=0
addata23=0
addata24=0


with open('shuju.txt','r+') as f:
    for i in f:
      try:
        url=re.findall(url1,str(i))
        with open('fenbu.txt','a+') as fi:
            url2=bs[a].strip()+'  '+url[0]
            fi.write(url2+'\n')
        if '00007058' in i or '00007059' in i or '00006904' in i or '00007073' in i or '00007074' in i or '00007081' in i or '00007084' in i or '00007085' in i or '00007089' in i or '00007065' in i or '00007066' in i or '00007079' in i or '00007071' in i or '00007088' in i:
            if re.findall(data01,i):
                ddata1 = ddata1 + 1
            if re.findall(data02,i):
                ddata2 = ddata2 + 1
            if re.findall(data03,i):
                ddata3 = ddata3 + 1
            if re.findall(data04,i):
                ddata4 = ddata4 + 1
            if re.findall(data05,i):
                ddata5 = ddata5 + 1
            if re.findall(data06,i):
                ddata6 = ddata6 + 1
            if re.findall(data07,i):
                ddata7 = ddata7 + 1
            if re.findall(data08,i):
                ddata8 = ddata8 + 1
            if re.findall(data09,i):
                ddata9 = ddata9 + 1
            if re.findall(data10,i):
                ddata10 = ddata10 + 1
            if re.findall(data11,i):
                ddata11 = ddata11 + 1
            if re.findall(data12,i):
                ddata12 = ddata12 + 1
            if re.findall(data13,i):
                ddata13 = ddata13 + 1
            if re.findall(data14,i):
                ddata14 = ddata14 + 1
            if re.findall(data15,i):
                ddata15 = ddata15 + 1
            if re.findall(data16,i):
                ddata16 = ddata16 + 1
            if re.findall(data17,i):
                ddata17 = ddata17 + 1
            if re.findall(data18,i):
                ddata18 = ddata18 + 1
            if re.findall(data19,i):
                ddata19 = ddata19 + 1
            if re.findall(data20,i):
                ddata20 = ddata20 + 1
            if re.findall(data21,i):
                ddata21 = ddata21 + 1
            if re.findall(data22,i):
                ddata22 = ddata22 + 1
            if re.findall(data23,i):
                ddata23 = ddata23 + 1
            if re.findall(data24,i):
                ddata24 = ddata24 + 1
            with open('userfrom.txt', 'a+') as fi:
                url2 = userip[a].strip() + '  ' + userdizhi[a].strip()
                fi.write(url2 + '\n')
            if '00007065' in i:
                username17065=str(re.findall(username7065,i))
                password17065=str(re.findall(password7065,i))
                realname17065=re.findall(realname7065,i)
                tel17065 = str(re.findall(tel7065, i))
                qq17065 = str(re.findall(qq7065, i))
                email17065 = str(re.findall(email7065, i))
                if realname17065!=['']:
                    with open('00007065.txt','a+') as f7065:
                        f7065.write('用户名：'+username17065+'   密码：'+password17065+'   真实姓名：[\''+urllib.unquote(realname17065[0])+'\']   电话：'+tel17065+'   QQ：'+qq17065+'   Email：'+email17065+'\n')
                else:
                    with open('00007065.txt','a+') as f7065:
                        f7065.write('用户名：'+username17065+'   密码：'+password17065+'   真实姓名：'+str(realname17065)+'   电话：'+tel17065+'   QQ：'+qq17065+'   Email：'+email17065+'\n')
            if '00007066' in i:
                username17066 = str(re.findall(username7066, i))
                password17066 = str(re.findall(password7066, i))
                tel17066 = str(re.findall(tel7066, i))
                with open('00007066.txt', 'a+') as f7066:
                    f7066.write('用户名：' + username17066 + '   密码：' + password17066 + '   电话：' + tel17066  + '\n')
            if '00007079' in i:
                username17079=str(re.findall(username7079,i))
                password17079=str(re.findall(password7079,i))
                realname17079=re.findall(realname7079,i)
                tel17079 = str(re.findall(tel7079, i))
                qq17079 = str(re.findall(qq7079, i))
                if realname17079!=['']:
                    with open('00007079.txt','a+') as f7079:
                        f7079.write('用户名：'+username17079+'   密码：'+password17079+'   真实姓名：[\''+urllib.unquote(realname17079[0])+'\']   电话：'+tel17079+'   QQ：'+qq17079+'\n')
                else:
                    with open('00007079.txt','a+') as f7079:
                        f7079.write('用户名：'+username17079+'   密码：'+password17079+'   真实姓名：'+str(realname17079)+'   电话：'+tel17079+'   QQ：'+qq17079+'\n')
            if '00007071' in i:
                username17071=str(re.findall(username7071,i))
                password17071=str(re.findall(password7071,i))
                realname17071=re.findall(realname7071,i)
                tel17071 = str(re.findall(tel7071, i))
                if realname17071!=['']:
                    with open('00007071.txt','a+') as f7071:
                        f7071.write('用户名：'+username17071+'   密码：'+password17071+'   真实姓名：[\''+urllib.unquote(realname17071[0])+'\']   电话：'+tel17071+'\n')
                else:
                    with open('00007071.txt','a+') as f7071:
                        f7071.write('用户名：'+username17071+'   密码：'+password17071+'   真实姓名：'+str(realname17071)+'   电话：'+tel17071+'\n')
            if '00007088' in i:
                username17088=str(re.findall(username7088,i))
                password17088=str(re.findall(password7088,i))
                realname17088=re.findall(realname7088,i)
                tel17088 = str(re.findall(tel7088, i))
                qq17088 = str(re.findall(qq7088, i))
                if realname17088!=['']:
                    with open('00007088.txt','a+') as f7088:
                        f7088.write('用户名：'+username17088+'   密码：'+password17088+'   真实姓名：[\''+urllib.unquote(realname17088[0])+'\']   电话：'+tel17088+'   QQ：'+qq17088+'\n')
                else:
                    with open('00007088.txt','a+') as f7088:
                        f7088.write('用户名：'+username17088+'   密码：'+password17088+'   真实姓名：'+str(realname17088)+'   电话：'+tel17088+'   QQ：'+qq17088+'\n')
        if '00007052' in i or '00007054' in i or '00006903' in i or '00007055' in i or '00007056' in i or '00007057' in i or '00007072' in i or '00007080' in i:
            if re.findall(data01,i):
                dddata1 = dddata1 + 1
            if re.findall(data02,i):
                dddata2 = dddata2 + 1
            if re.findall(data03,i):
                dddata3 = dddata3 + 1
            if re.findall(data04,i):
                dddata4 = dddata4 + 1
            if re.findall(data05,i):
                dddata5 = dddata5 + 1
            if re.findall(data06,i):
                dddata6 = dddata6 + 1
            if re.findall(data07,i):
                dddata7 = dddata7 + 1
            if re.findall(data08,i):
                dddata8 = dddata8 + 1
            if re.findall(data09,i):
                dddata9 = dddata9 + 1
            if re.findall(data10,i):
                dddata10 = dddata10 + 1
            if re.findall(data11,i):
                dddata11 = dddata11 + 1
            if re.findall(data12,i):
                dddata12 = dddata12 + 1
            if re.findall(data13,i):
                dddata13 = dddata13 + 1
            if re.findall(data14,i):
                dddata14 = dddata14 + 1
            if re.findall(data15,i):
                dddata15 = dddata15 + 1
            if re.findall(data16,i):
                dddata16 = dddata16 + 1
            if re.findall(data17,i):
                dddata17 = dddata17 + 1
            if re.findall(data18,i):
                dddata18 = dddata18 + 1
            if re.findall(data19,i):
                dddata19 = dddata19 + 1
            if re.findall(data20,i):
                dddata20 = dddata20 + 1
            if re.findall(data21,i):
                dddata21 = dddata21 + 1
            if re.findall(data22,i):
                dddata22 = dddata22 + 1
            if re.findall(data23,i):
                dddata23 = dddata23 + 1
            if re.findall(data24,i):
                dddata24 = dddata24 + 1
            with open('dailifrom.txt', 'a+') as fi:
                url2 = userip[a].strip() + '  ' + userdizhi[a].strip()
                fi.write(url2 + '\n')
            if '00007052' in i:
                url = re.findall(url1, i)
                user = re.findall(username7065, i)
                with open('dailizh.txt','a+') as f:
                    f.write(url[0]+'    '+user[0]+'\n')
            if '00007054' in i:
                url = re.findall(url1, i)
                user = re.findall(user7054, i)
                with open('dailizh.txt','a+') as f:
                    f.write(url[0]+'    '+user[0]+'\n')
            if '00006903' in i:
                url = re.findall(url1, i)
                user = re.findall(user6903, i)
                with open('dailizh.txt','a+') as f:
                    f.write(url[0]+'    '+user[0]+'\n')
            if '00007055' in i:
                url = re.findall(url1, i)
                user = re.findall(user7055, i)
                with open('dailizh.txt','a+') as f:
                    f.write(url[0]+'    '+user[0]+'\n')
            if '00007056' in i:
                url = re.findall(url1, i)
                user = re.findall(user7056, i)
                with open('dailizh.txt','a+') as f:
                    f.write(url[0]+'    '+user[0]+'\n')
            if '00007057' in i:
                url = re.findall(url1, i)
                user = re.findall(username7065, i)
                with open('dailizh.txt','a+') as f:
                    f.write(url[0]+'    '+user[0]+'\n')
            if '00007072' in i:
                url = re.findall(url1, i)
                user = re.findall(user7072, i)
                with open('dailizh.txt','a+') as f:
                    f.write(url[0]+'    '+user[0]+'\n')
            if '00007080' in i:
                username=str(re.findall(username7065,i))
                password=str(re.findall(password7071,i))
                realname=re.findall(dailiname,i)
                tel = str(re.findall(dailitel, i))
                weixin = str(re.findall(dailiweixin, i))
                email = str(re.findall(dailiemail, i))
                card = str(re.findall(dailicard, i))
                if realname!=['']:
                    with open('00007080.txt','a+') as f7065:
                        f7065.write('用户名：'+username+'   密码：'+password+'   真实姓名：[\''+urllib.unquote(realname[0])+'\']   电话：'+tel+'   weixin：'+weixin+'   Email：'+email+'\n')
                else:
                    with open('00007080.txt','a+') as f7065:
                        f7065.write('用户名：'+username+'   密码：'+password+'   真实姓名：'+str(realname)+'   电话：'+tel+'   weixin：'+weixin+'   Email：'+email+'\n')
        if '00007060' in i or '00007061' in i or '00007062' in i or '00007063' in i:
            with open('adminfrom.txt', 'a+') as fi:
                url2 = userip[a].strip() + '  ' + userdizhi[a].strip()
                fi.write(url2 + '\n')
            if re.findall(data01, i):
                addata1 = addata1 + 1
            if re.findall(data02, i):
                addata2 = addata2 + 1
            if re.findall(data03, i):
                addata3 = addata3 + 1
            if re.findall(data04, i):
                addata4 = addata4 + 1
            if re.findall(data05, i):
                addata5 = addata5 + 1
            if re.findall(data06, i):
                addata6 = addata6 + 1
            if re.findall(data07, i):
                addata7 = addata7 + 1
            if re.findall(data08, i):
                addata8 = addata8 + 1
            if re.findall(data09, i):
                addata9 = addata9 + 1
            if re.findall(data10, i):
                addata10 = addata10 + 1
            if re.findall(data11, i):
                addata11 = addata11 + 1
            if re.findall(data12, i):
                addata12 = addata12 + 1
            if re.findall(data13, i):
                addata13 = addata13 + 1
            if re.findall(data14, i):
                addata14 = addata14 + 1
            if re.findall(data15, i):
                addata15 = addata15 + 1
            if re.findall(data16, i):
                addata16 = addata16 + 1
            if re.findall(data17, i):
                addata17 = addata17 + 1
            if re.findall(data18, i):
                addata18 = addata18 + 1
            if re.findall(data19, i):
                addata19 = addata19 + 1
            if re.findall(data20, i):
                addata20 = addata20 + 1
            if re.findall(data21, i):
                addata21 = addata21 + 1
            if re.findall(data22, i):
                addata22 = addata22 + 1
            if re.findall(data23, i):
                addata23 = addata23 + 1
            if re.findall(data24, i):
                addata24 = addata24 + 1
            if '00007060' in i:
                url = re.findall(url1, i)
                user = re.findall(admin7060, i)
                with open('adminzh.txt','a+') as f:
                    f.write(url[0]+'    '+user[0]+'\n')
            if '00007061' in i:
                url = re.findall(url1, i)
                user = re.findall(admin7061, i)
                with open('adminzh.txt','a+') as f:
                    f.write(url[0]+'    '+user[0]+'\n')
            if '00007062' in i:
                url = re.findall(url1, i)
                user = re.findall(admin7061, i)
                with open('adminzh.txt','a+') as f:
                    f.write(url[0]+'    '+user[0]+'\n')
            if '00007063' in i:
                url = re.findall(url1, i)
                user = re.findall(username7065, i)
                with open('adminzh.txt','a+') as f:
                    f.write(url[0]+'    '+user[0]+'\n')
        a = a + 1
      except:
          print '错误'
          a = a + 1

print '01点赌博网站登录次数:'+str(ddata1)+'，02点赌博网站登录次数:'+str(ddata2)+'，03点赌博网站登录次数:'+str(ddata3)+'，04点赌博网站登录次数:'+str(ddata4)+'，05点赌博网站登录次数:'+str(ddata5)+'，06点赌博网站登录次数:'+str(ddata6)+'，07点赌博网站登录次数:'+str(ddata7)+'，08点赌博网站登录次数:'+str(ddata8)+'，09点赌博网站登录次数:'+str(ddata9)+'，10点赌博网站登录次数:'+str(ddata10)+'，11点赌博网站登录次数:'+str(ddata11)+'，12点赌博网站登录次数:'+str(ddata12)+'，13点赌博网站登录次数:'+str(ddata13)+'，14点赌博网站登录次数:'+str(ddata14)+'，15点赌博网站登录次数:'+str(ddata15)+'，16点赌博网站登录次数:'+str(ddata16)+'，17点赌博网站登录次数:'+str(ddata17)+'，18点赌博网站登录次数:'+str(ddata18)+'，19点赌博网站登录次数:'+str(ddata19)+'，20点赌博网站登录次数:'+str(ddata20)+'，21点赌博网站登录次数:'+str(ddata21)+'，22点赌博网站登录次数:'+str(ddata22)+'，23点赌博网站登录次数:'+str(ddata23)+'，24点赌博网站登录次数:'+str(ddata24)+'\n'
print '01点赌博网站代理登录次数:'+str(dddata1)+'，02点赌博网站代理登录次数:'+str(dddata2)+'，03点赌博网站代理登录次数:'+str(dddata3)+'，04点赌博网站代理登录次数:'+str(dddata4)+'，05点赌博网站代理登录次数:'+str(dddata5)+'，06点赌博网站代理登录次数:'+str(dddata6)+'，07点赌博网站代理登录次数:'+str(dddata7)+'，08点赌博网站代理登录次数:'+str(dddata8)+'，09点赌博网站代理登录次数:'+str(dddata9)+'，10点赌博网站代理登录次数:'+str(dddata10)+'，11点赌博网站代理登录次数:'+str(dddata11)+'，12点赌博网站代理登录次数:'+str(dddata12)+'，13点赌博网站代理登录次数:'+str(dddata13)+'，14点赌博网站代理登录次数:'+str(dddata14)+'，15点赌博网站代理登录次数:'+str(dddata15)+'，16点赌博网站代理登录次数:'+str(dddata16)+'，17点赌博网站代理登录次数:'+str(dddata17)+'，18点赌博网站代理登录次数:'+str(dddata18)+'，19点赌博网站代理登录次数:'+str(dddata19)+'，20点赌博网站代理登录次数:'+str(dddata20)+'，21点赌博网站代理登录次数:'+str(dddata21)+'，22点赌博网站代理登录次数:'+str(dddata22)+'，23点赌博网站代理登录次数:'+str(dddata23)+'，24点赌博网站代理登录次数:'+str(dddata24)+'\n'
print '01点赌博网站管理登录次数:'+str(addata1)+'，02点赌博网站管理登录次数:'+str(addata2)+'，03点赌博网站管理登录次数:'+str(addata3)+'，04点赌博网站管理登录次数:'+str(addata4)+'，05点赌博网站管理登录次数:'+str(addata5)+'，06点赌博网站管理登录次数:'+str(addata6)+'，07点赌博网站管理登录次数:'+str(addata7)+'，08点赌博网站管理登录次数:'+str(addata8)+'，09点赌博网站管理登录次数:'+str(addata9)+'，10点赌博网站管理登录次数:'+str(addata10)+'，11点赌博网站管理登录次数:'+str(addata11)+'，12点赌博网站管理登录次数:'+str(addata12)+'，13点赌博网站管理登录次数:'+str(addata13)+'，14点赌博网站管理登录次数:'+str(addata14)+'，15点赌博网站管理登录次数:'+str(addata15)+'，16点赌博网站管理登录次数:'+str(addata16)+'，17点赌博网站管理登录次数:'+str(addata17)+'，18点赌博网站管理登录次数:'+str(addata18)+'，19点赌博网站管理登录次数:'+str(addata19)+'，20点赌博网站管理登录次数:'+str(addata20)+'，21点赌博网站管理登录次数:'+str(addata21)+'，22点赌博网站管理登录次数:'+str(addata22)+'，23点赌博网站管理登录次数:'+str(addata23)+'，24点赌博网站管理登录次数:'+str(addata24)+'\n'

