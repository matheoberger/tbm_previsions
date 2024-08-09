from django.shortcuts import render
from django.http import HttpResponse
import requests


def previsions(request):
    response = requests.get('https://opendata.bordeaux-metropole.fr/api/records/1.0/search/?dataset=ci_courb_a&rows=193')
    previsions = response.json()
    records = previsions['records']

    previsions_data = []       

    for record in records:
        fields = record['fields']
        bm_heure = fields.get('bm_heure')
        bm_prevision = fields.get('bm_prevision')

        # print(f'bm_heure: {bm_heure}')
        # print(f'bm_prevision: {bm_prevision}')

        previsions_data.append({
            'bm_heure': bm_heure,
            'bm_prevision': bm_prevision
        })

    return render(request, "previsions.html", {'previsions_data': previsions_data})