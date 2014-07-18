import urllib
from bs4 import BeautifulSoup

basicurl = "http://media.khu.ac.kr/khul_eng/sublist.asp?code1=1032006022804&code_b=2010100110000002&page=%(i)s&field=&keyword="


for i in range(1, 6):
	htmltext = urllib.urlopen(basicurl % {'i' : i}).read()


soup = BeautifulSoup(htmltext, from_encoding="utf-8")

for each in soup.findAll('td', attrs={'class': 'btt'}):
	print "article : " + each.a.string

	




	





	

	
	   
	

