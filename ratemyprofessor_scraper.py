import requests
import json
import time
import pymongo

db = pymongo.MongoClient().local.ratemyprofs

counter = 0

for i in range(1,210):
	
	query = "http://www.ratemyprofessors.com/filter/professor/?department=&institution=California+State+University%2C+Northridge&page="+str(i)+"&filter=teacherlastname_sort_s+asc&query=*%3A*&queryoption=TEACHER&queryBy=schoolId&sid=163"

	
	try:
		page = requests.get(query)
		jsonpage = json.loads(page.content)
		professorlist = jsonpage['professors']

		if len(professorlist)>0:
			for prof in professorlist:
				if db.find_one({"tid":int(prof['tid'])}) is None:
					db.insert(prof)
		print "page "+str(i)+" "+'\xF0\x9F\x98\x8F'
	except:
		pass

	time.sleep(1)