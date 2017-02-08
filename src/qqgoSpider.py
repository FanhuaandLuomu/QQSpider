# coding:utf-8
# 使用selenium对http://g.gogoqq.com进行爬取qq空间背景音乐
# ps:2016.1.27写的爬虫，当时上述网站还能正常访问qq空间，
# 现在竟然崩掉了，能打开网站，但是网站的功能已经没了
# 所有该爬虫已无实际用途，而且限于当时的能力，爬虫粗糙，惭愧
# 好在当时爬的数据还有一部分，所以仅仅围绕爬的数据做点简单分析。
# 限于该网站当时就很烂==+水平有限，改爬虫仅仅爬取qq昵称和简单的个人信息
# 设置一个种子id,从访客和留言板中提取用户qq号增量爬取。
from selenium import webdriver
from scrapy.selector import Selector
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from scrapy.selector import Selector
import lxml.html.soupparser as soupparser
import time
import re

def getInfoToFile(qqid, browser, filename):
	url_info = 'http://g.gogoqq.com/onLine.htm?uin=' + qqid
	# url = url_info.replace('qqid', qqid)
	# print url
	f = open(filename, 'a')
	f.write(qqid + '\n')
	f.close()
	browser.get(url_info)
	time.sleep(2)
	page = browser.page_source 
	# elems=Selector(text=page).xpath('//div[@id="article_list"]/div[@class="list_item article_item"]/div[1]/h1/span/a/text()')
	# for item in elems:
	# 	print item.extract()
	
	try:
		dom = soupparser.fromstring(page)
		name = dom.xpath(u'//*[@id="list"]/dd[1]')
		f = open(filename, 'a')
		if(name != None):
			name = name[0].text.strip()
			print name
			f.write(qqid + ' ' + name + ' ')
		info = dom.xpath(u'//*[@id="list"]/dd[2]')
		if(info != None):
			info = info[0].text.strip()
			print info
			f.write(info + '\n')
		f.close()

	except Exception, e:
		print 'err:', e

# def getInfoToFile2(qqid,browser,filename):
# 	url_info = 'http://g.gogoqq.com/onLine.htm?uin=' + qqid
# 	browser.get(url_info)
# 	time.sleep(2)


def getConcerns(qqid, browser):
	url_visit = 'http://g.gogoqq.com/relatedList.htm?uin=' + qqid
	# url=url_visit.replace('qqid',qqid)
	qqList = []
	browser.get(url_visit)
	time.sleep(1)
	page = browser.page_source
	
	dom = soupparser.fromstring(page)
	qqL = dom.xpath(u'//*[@id="searchlist"]/a/span')
	for item in qqL:
		item = item.text.strip()
		# print item
		qqList.append(item)
	print 'len(Concerns):'+str(len(qqList))
	return qqList

def getLeaveWords(qqid, browser):
	url_lwords = 'http://g.gogoqq.com/leaveWords.htm?uin=' + qqid
	browser.get(url_lwords)
	time.sleep(1)
	browser.maximize_window() 
	page = browser.page_source
	
	liList = Selector(text = page).xpath('//*[@id="list"]/li')
	print len(liList)
	List0 = []
	if(len(liList) > 0):
		try:
			WebDriverWait(browser, 4, 0.5).until(lambda item:item.find_element_by_xpath('//*[@id="btnNext"]').is_displayed())
			more = browser.find_element_by_xpath('//*[@id="btnNext"]')
			k = 0
			while(1 and k<20):
				more.click()
				print 'load more!'
				time.sleep(1)
				WebDriverWait(browser, 4, 0.5).until(lambda item:item.find_element_by_xpath('//*[@id="btnNext"]').is_displayed())
				more = browser.find_element_by_xpath('//*[@id="btnNext"]')
				k += 1
		except Exception, e:
			print 'load success!'
		page = browser.page_source
		
		ul = Selector(text = page).xpath(u'//*[@id="list"]/li')
		for item in ul:
			qqnick = item.xpath('//div/span[1]/a/text()')[0].extract()
			qqid = item.xpath('//div/span[1]/a/@href')[0].extract()
			qqid = re.findall(r'uin=(.*)', qqid, re.S)[0]
			List0.append(qqid)
	print 'len(leaveWords):'+str(len(List0))
	return List0

if __name__ == '__main__':
	IE = r'C:\Program Files\Internet Explorer\IEDriverServer.exe'
	print 'start'
	# url='http://www.court.gov.cn/zgcpwsw/zxws/index.htm' 
	rootId = '1601441611'
	filename = rootId + '_new .txt'
	qqList = []
	# rootUrl=url_visit.replace('qqid',rootId)
	qqList.append(rootId)
	vistedList = []
	# url='http://blog.csdn.net/zouxy09/article/category/1333962'
	browser = webdriver.Ie(IE)
	# browser.maximize_window()		
	# browser=webdriver.Firefox()
	# time.sleep(10)
	# browser.close()
	while(len(qqList) > 0):
		if(qqList[0] not in vistedList):
			getInfoToFile(qqList[0], browser, filename)
			# if(qqList[0]=='1601441611'):
			# 	print 'find!!!'
			vistedList.append(qqList[0])
			if len(qqList)<50000:
				qqList += getConcerns(qqList[0], browser)
				qqList += getLeaveWords(qqList[0], browser)
		qqList.remove(qqList[0])
		print 'len(qqList):' + str(len(qqList))
		print 'len(vistedList):' + str(len(vistedList))
	print '..'
	browser.quit()
		

