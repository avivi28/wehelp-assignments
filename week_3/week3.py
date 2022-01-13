import urllib.request as request
import json
src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
    data=json.load(response)
clist=data['result']['results']

with open("data.csv","w", encoding="utf-8")as file:
    for travel in clist:
        address=travel["address"]
        wanted_address=(address.split()[1][:3])
        link=travel['file']
        wanted_link=(link.split('https')[1])
        file.write(travel['stitle']+","+wanted_address+","+travel['longitude']+","+travel['latitude']+",https"+wanted_link+'\n')
        
with open("connect.txt","w", encoding="utf-8")as file:
    for image in clist:
        link=travel['file']
        wanted_link=(link.split('https')[1])
        file.write("["+'{"url":"https'+wanted_link+'"},'+'\n'+"]")