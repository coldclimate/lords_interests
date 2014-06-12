#!/usr/local/bin/python

from bs4 import BeautifulSoup

soup = BeautifulSoup(open("data/A.html"))
results = []
top_level = soup.find_all("table", class_="lordsinteresttable")

for lord in top_level:
	lord_result={}
	lord_result['name'] = lord.find_all("td", class_="lordsinterestmember")[0].string
	lord_result['name'] = lord.find_all("td", class_="lordsinterestmember")[0].string
	results.append(lord_result)

print results