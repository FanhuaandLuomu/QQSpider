#coding:utf-8

from __future__ import division
import re
from pylab import *
import requests
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def pre_deal(filename): #预处理 提取信息
	qqInfoList=[]
	f=open(filename,'r')
	for line in f.readlines():
		if(len(line.split())>1):
			qqInfoList.append(line.strip())
	return qqInfoList

def showInfo(qqInfoList): #显示信息
	for line in qqInfoList:
		print line

def sexCount(qqInfoList): #性别比例分析
	girl=[]
	boy=[]
	other=[]
	for item in qqInfoList:
		if(u'女' in item):
			girl.append(item)
		elif(u'男' in item):
			boy.append(item)
		else:
			other.append(item)
	return girl,boy,other

def draw(listX,listY,type):
	figure(1,figsize=(10,10))
	ax=axes([0.1,0.1,0.8,0.8])
	fracs=listY
	labels=listX
	#explode=(0,0,0.08)
	if(type==0):
		colors=('g','r','y','b','0.75','#00FFFF','c','m','darkslategray')
		t='Age Distribution'
	else:
		colors=('g','r','y','b','0.75','#00FFFF','c','m','darkslategray','w','0.25','#2F0F4F')
		t='Constellations Distribution'
	pie(fracs,labels=labels,
		autopct='%1.1f%%',shadow=True,startangle=90,colors=colors)
	title(t)
	show()

def ageCount(qqInfoList):
	ageList=[]
	time2010=(0,2016-2010)
	time00=(2016-2009,2016-2000)
	time90=(2016-1999,2016-1990)
	time80=(2016-1989,2016-1980)
	time70=(2016-1979,2016-1970)
	time60=(2016-1969,2016-1960)
	time50=(2016-1959,2016-1950)
	time40=(2016-1949,2016-1940)
	count2010=0
	count00=0
	count90=0
	count80=0
	count70=0
	count60=0
	count50=0
	count40=0
	other=0
	#otherList=[]
	unknown=0
	for item in qqInfoList:
		if(u'存在了' in item):
			age=re.findall(r'\xb4\xe6\xd4\xda\xc1\xcb(.*?)\xc4\xea',item)[0]
			#print age
			age=int(age)
			if(age>=time2010[0] and age<=time2010[1]):
				count2010+=1
			elif(age>=time00[0] and age<=time00[1]):
				count00+=1
			elif(age>=time90[0] and age<=time90[1]):
				count90+=1
			elif(age>=time80[0] and age<=time80[1]):
				count80+=1
			elif(age>=time70[0] and age<=time70[1]):
				count70+=1
			elif(age>=time60[0] and age<=time60[1]):
				count60+=1
			elif(age>=time50[0] and age<=time50[1]):
				count50+=1
			elif(age>=time40[0] and age<=time40[1]):
				count40+=1
			else:
				other+=1
				#otherList.append(age)
			ageList.append(age)
		else:
			unknown+=1
	print 'ageLen:',len(ageList)
	print 'unknown age:',unknown

	print '\ntime2010:',count2010,'[%.2f%%]' %(count2010/len(ageList)*100)
	print 'time00:',count00,'[%.2f%%]' %(count00/len(ageList)*100)
	print 'time90:',count90,'[%.2f%%]' %(count90/len(ageList)*100)
	print 'time80:',count80,'[%.2f%%]' %(count80/len(ageList)*100)
	print 'time70:',count70 ,'[%.2f%%]' %(count70/len(ageList)*100)
	print 'count60:',count60,'[%.2f%%]' %(count60/len(ageList)*100)
	print 'count50:',count50,'[%.2f%%]' %(count50/len(ageList)*100)
	print 'count40:',count40,'[%.2f%%]' %(count40/len(ageList)*100)
	print 'other:',other,'[%.2f%%]' %(other/len(ageList)*100)
	listX=['10-16','00-09','90-09','80-89','70-79','60-69','50-59','40-49','other']
	listY=[count2010,count00,count90,count80,count70,count60,count50,count40,other]
	draw(listX,listY,0)

def xinzuo(qqInfoList):  #星座分析
	#白羊座(3.21-4.19)、金牛座(4.20-5.20)、双子座(5.21-6.21)、巨蟹座(6.22-7.22)
	#狮子座(7.23-8.22)、处女座(8.23-9.22)、天秤座(9.23-10.23)、天蝎座(10.24-11.22)
	#射手座(11.23-12.21)、摩羯座(12.22-1.19)、水瓶座(1.20-2.18)、双鱼座(2.19-3.20)
	#xz=[baiy,jinn,shuangz,jux,shiz,chun,tianc,tianx,shes,moj,shuip,shuangy,other]  
	baiy=[]
	jinn=[]
	shuangz=[]
	jux=[]
	shiz=[]
	chun=[]
	tianc=[]
	tianx=[]
	shes=[]
	moj=[]
	shuip=[]
	shuangy=[]
	other=[]
	for item in qqInfoList:
		if(u'白羊座' in item):
			baiy.append(item)
		elif(u'金牛座' in item):
			jinn.append(item)
		elif(u'双子座' in item):
			shuangz.append(item)
		elif(u'巨蟹座' in item):
			jux.append(item)
		elif(u'狮子座' in item):
			shiz.append(item)
		elif(u'处女座' in item):
			chun.append(item)
		elif(u'天秤座' in item):
			tianc.append(item)
		elif(u'天蝎座' in item):
			tianx.append(item)
		elif(u'射手座' in item):
			shes.append(item)
		elif(u'魔羯座' in item):
			moj.append(item)
		elif(u'水瓶座' in item):
			shuip.append(item)
		elif(u'双鱼座' in item):
			shuangy.append(item)
		else:
			other.append(item)

	print u'白羊座:%d' %(len(baiy))
	print u'金牛座:%d' %(len(jinn))
	print u'双子座:%d' %(len(shuangz))
	print u'巨蟹座:%d' %(len(jux))
	print u'狮子座:%d' %(len(shiz))
	print u'处女座:%d' %(len(chun))
	print u'天秤座:%d' %(len(tianc))
	print u'天蝎座:%d' %(len(tianx))
	print u'射手座:%d' %(len(shes))
	print u'摩羯座:%d' %(len(moj))
	print u'水瓶座:%d' %(len(shuip))
	print u'双鱼座:%d' %(len(shuangy))
	print u'未  知:%d' %(len(other))
	listX=['Aries','Taurus','Gemini','Cancer','Leo','Virgo','Libra','Scorpio','Sagittarius','Capricorn',u'Aquarius','Pisces']
	listY=[len(baiy),len(jinn),len(shuangz),len(jux),len(shiz),len(chun),len(tianc),len(tianx),len(shes),len(moj),len(shuip),len(shuangy)]
	draw(listX,listY,1)
 
if __name__ == '__main__':
	filelist=['1049755192.txt','1049755192_new.txt','1049755192_new2.txt',
	'1049755192_new3.txt','1049755192_new4.txt','1049755192_new5.txt','1601441611.txt']
	#filename='1049755192_new4.txt'
	# filename='1601441611.txt'
	qqInfoList=[]
	for filename in filelist:
		qqInfoList+=pre_deal(filename)
	qqInfoList=list(set(qqInfoList))
	showInfo(qqInfoList)
	print 'qqInfoList:%d' %(len(qqInfoList))
	girl,boy,other=sexCount(qqInfoList)
	print 'girl:%d(%.3f) boy:%d(%.3f) other:%d' %(len(girl),len(girl)/len(qqInfoList),len(boy),len(boy)/len(qqInfoList),len(other))
	xinzuo(qqInfoList)
	ageCount(qqInfoList)