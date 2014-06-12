#!/usr/local/bin/python

from bs4 import BeautifulSoup

soup = BeautifulSoup(open("data/A.html"))
results = []
top_level = soup.find_all("table", class_="lordsinteresttable")

for lord in top_level:
	lord_result={}
	lord_result['name'] = lord.find_all("td", class_="lordsinterestmember")[0].string
	lord_result['pods']=[]
	pod = {}
	for row in lord.find_all("td"):
		try:
			the_class = row['class'][0]

		except KeyError:
			the_class = "Notset"

		if the_class == "lordsinterestmember":
		    print ''
		elif the_class == "lordsinterestcategory":
		    print ''
		    # file the existing one
		    lord_result['pods'].append(pod)
		    pod = {'type' : row.string, 'entries':[]}
		else:
		    pod['entries'].append(row.string)

	results.append(lord_result)

import json
print json.dumps(results,sort_keys=True, indent=4)


#print results