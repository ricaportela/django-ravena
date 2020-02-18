#!/usr/bin/env python
# coding: utf-8
import json
import pandas as pd
import requests
from pygbif import species


def gbiftaxon(request, taxon):
    termo = "Handroanthus"
    url = "http://api.gbif.org/v1/species/search"
    params = {'q': termo}
    resp = requests.get(url, params=params)
    results = resp.json()['results']
    context = {'context': json.dumps(results)}
    


gbiftaxon()

def specieplus():
    api_token = 'DokjY7GSkHnt7KH2qG1YHwtt'
    myUrl = 'https://api.speciesplus.net/api/v1/taxon_concepts.xml?name=Mammalia'
    headers = {'X-Authentication-Token': api_token}


    response = requests.get(myUrl, headers=headers)

    print(response.text)

# def get_nextpage():
#     url = 'https://example.zendesk.com/api/v2/help_center/sections/200646/articles.json'
#     while url:
#         response = session.get(url)
#         data = response.json()
#         for article in data['articles']:
#             print(article['title'])
#         url = data['next_page']

# def read_api():
#     termo = ["Handroanthus", "Ursus"]
#     espec = species.name_lookup(q=termo[1], limit=2000)
#     lst = espec['results']
#     df = pd.DataFrame(lst)
    
#     # new_df = df[['taxonKey', 'scientificName', 'canonicalName', 'taxonomicStatus', 'rank', 'genus']]
#     # df = pd.DataFrame(espec['results'])
    
#     # grupo1 = df.groupby([ 'key', 'scientificName', 'rank','taxonomicStatus' ])
    
#     # for k, v in grupo1.groups.items():
#     #     print(k)

#     has_next_key = False
#     nextKey = ""
    
#     if "next_key" in jsonData:
#         has_next_key = True
#         nextKey = jsonData["next_key"]
    
#     while has_next_key:
#         data = {"limit_count":100, "limit_size":10000,"curr_key":nextKey}
#         params = {"data":json.dumps(data, separators=(",", ":"))}
    
#         req = requests.get(url, params=params, headers=headers).json()  ## this should do GET request for the third page and so on...
#         if "next_key" in req:
#             nextKey = req["next_key"]
#             print nextKey # this returns "3321" which is the value for "next_key" in second page
#         else:
#             has_next_key = False
#             # no next_key, stop the loop
