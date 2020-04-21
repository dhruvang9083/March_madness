import json
import csv

with open('/Users/dhruvangpatel/Desktop/covid_19.json') as f:
    covid19_data = json.load(f)
    recovered = 0
    deaths = 0
    confirmed = 0
    for data in covid19_data:
    	for case in covid19_data[data]:
    		deaths += case['deaths']
    		confirmed += case['confirmed']
    		recovered += case['recovered']

print("Total deaths cases : ", deaths)
print("Total confirmed cases : ", confirmed)
print("Total recovered cases : ",recovered)
