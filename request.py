import requests


url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'opened_by':24,'location':98,'ID_caller':2403,'Category_id':164,'ID':86,'created_at_minute':49})
print(r.json())