#!/usr/bin/env python
# coding: utf-8
import json
import requests


termos = ["Handroanthus", "Ursus"]

url = "http://api.gbif.org/v1/species/search"
params = {'q': termos[1]}
resp = requests.get(url, params=params)
results = resp.json()['results']
context = {'context': json.dumps(results)}

print(context)

end_of_records = False
previous_offset = previous_limit = offset = 0
total_results = []

while not end_of_records:
    offset = previous_offset + previous_limit

    url = "http://api.gbif.org/v1/species/search"
    params = {'q': termos[1], 'offset': offset}
    resp = requests.get(url, params=params)

    for result in resp.json()['results']:
        total_results.append({"scientificName": result["scientificName"],
                              "taxonomicStatus": result["taxonomicStatus"],
                              "rank": result["rank"]})

    previous_offset = resp.json()['offset']
    previous_limit = resp.json()['limit']
    end_of_records = resp.json()['endOfRecords']

#
# Aqui eu tenho total_results completo.
# Chamar pandas.
# ...
# retornar resultado pro usuário.
