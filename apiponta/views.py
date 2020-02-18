from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from http import HTTPStatus
import json
import requests
import pandas as pd
from pygbif import species


def get_species(request):
    """Endpoint que responde com resultado da busca.

    Modelo da URL: www.example.com/quati/species/search/?q=puma
    
    local http://127.0.0.1:8000/quati/species/search/?q=Puma

    """
    
    termo = request.GET.get("q", "") .strip()
    if not termo:
        data = []
        return HttpResponse(json.dumps(data), content_type="application/json")

    results = _get_data_from_external_api(termo)
    if not results:
        return JsonResponse(data=[], status_code=HTTPStatus.NOT_FOUND)
    
    # final_results = _summarize_results_by_scientific_name(results)

    # final_results = [
    #     {"scienticName": "Puma", "rank": "Genus"},
    #     {"scienticName": "Puma roxo", "rank": "Outro Genus"},
    #     {"scienticName": "Puma Blanco", "rank": "Mais um Genus"},
    #     {"scienticName": "Puma Albino", "rank": "Genus"}
    # ]

    data =  json.dumps(results)

    return JsonResponse(data=results, safe=False)
    # return HttpResponse(final_results, content_type="application/json")

    # return JsonResponse(data=final_results, safe=False)
    # return JsonResponse(data=final_results, safe=False, status_code=HTTPStatus.OK)



def get_species_group(request):
    url = "http://api.gbif.org/v1/species/search"
    offset =  100
    limit = 100

    termo = request.GET.get("q", "").strip()
    if not termo:
        data = []
        return HttpResponse(json.dumps(data), content_type="application/json")

    params = {'q': termo,  'offset': offset, 'limit': limit}
    # results = requests.get(url, params=params).json()
    context = {
        'results': [
            {
                'scientificName': 'Ursus',
                'taxonomicStatus': 'ACCEPTED'
            },
            {
                'scientificName': 'Ursusx',
                'taxonomicStatus': 'ACCEPTED'
            },
            {
                'scientificName': 'AUrsus',
                'taxonomicStatus': 'ACCEPTED'
            },
        ]
    }
    data =  json.dumps(context)

    return HttpResponse(data)

def _get_data_from_external_api(termo):
    """Busca o termo an API externa e retorna lista com resultados."""

    end_of_records = False
    previous_offset = previous_limit = offset = 0
    total_results = []
    url = "http://api.gbif.org/v1/species/search"

    while not end_of_records:
        offset = previous_offset + previous_limit
        params = {'q': termo, 'offset': offset}
        resp = requests.get(url, params=params)
        if resp.status_code != HTTPStatus.OK:
            # logger.error("Erro ao acessar {url}/{params}: {resp.status_code} - {resp.text}")
            print("Erro ao acessar {url}/{params}: {resp.status_code} - {resp.text}")
            return []

        for result in resp.json()['results']:
            total_results.append({"scientificName": result.get('scientificName', "no scientific name"),
                                  "taxonomicStatus": result.get('taxonomicStatus', "no taxonomic status"),
                                  "rank": result.get('rank', 'no rank name')})

        previous_offset = int(resp.json()['offset'])
        previous_limit = int(resp.json()['limit'])
        end_of_records = bool(resp.json()['endOfRecords'])

    return total_results



def _summarize_results_by_scientific_name(results):
    """Summarize data by ScientificName."""

    #TODO usar pandas
    #TODO formatar resultado conforme estrutura abaixo:
    summarized_results = {
        'results': [
            {
                'scientificName': 'Ursus',
                'rank': 'Genus'
            },
            {
                'scientificName': 'Ursusx',
                'rank': 'Genus Others'
            },
            {
                'scientificName': 'AUrsus',
                'rank': 'Genux 12'
            },
        ]
    }
    results =  json.dumps(summarized_results)

    return HttpResponse(json.dumps(results), content_type="application/json")



# summarized_results = {
#                         "scientificName": "Puma",
#                          "rank": "XXX"
#                     }
# # data = json.dumps(summarized_results)

# return JsonResponse(summarized_results)
# # return HttpResponse(json.dumps(responseData), content_type="application/json")



# def get_with_gbif(resquest):
#     termo = ["Handroanthus", "Ursus"]
#     espec = species.name_lookup(q=termo[1], limit=2000)
#     lst = espec['results']
#     df = pd.DataFrame(lst)

#     new_df = df[['key', 'scientificName', 'canonicalName', 'taxonomicStatus', 'rank', 'genus']]
#     df = pd.DataFrame(espec['results'])

#     grupo1 = df.groupby([ 'key', 'scientificName', 'rank','taxonomicStatus' ])

#     type(grupo1)

#     for k, v in grupo1.groups.items():
#         print(k)

#     results =  k

#     return HttpResponse(results)



