#!/usr/bin/env python
# coding: utf-8
import json
import pandas as pd
from pygbif import species


termo = ["Handroanthus", "Ursus"]
espec = species.name_lookup(q=termo[1], limit=2000)
lst = espec['results']
df = pd.DataFrame(lst)

new_df = df[['taxonKey', 'scientificName', 'canonicalName', 'taxonomicStatus', 'rank', 'genus']]
df = pd.DataFrame(espec['results'])

grupo1 = df.groupby([ 'key', 'scientificName', 'rank','taxonomicStatus' ])

for k, v in grupo1.groups.items():
    print(k)
