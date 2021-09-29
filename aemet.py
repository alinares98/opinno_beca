import http.client

conn = http.client.HTTPSConnection("opendata.aemet.es")

headers = {
    'cache-control': "no-cache"
    }

conn.request("GET", "/opendata/api/prediccion/especifica/municipio/diaria/079?api_key=eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhbGJlcnRvbGluYXJlc2NvcnJhbGVzMTZAZ21haWwuY29tIiwianRpIjoiNDExMWUyMTgtNWQwYS00MGNjLTk1ODUtNTU2YmI3ZDhlOWY4IiwiaXNzIjoiQUVNRVQiLCJpYXQiOjE2MzI5Mjk2NTIsInVzZXJJZCI6IjQxMTFlMjE4LTVkMGEtNDBjYy05NTg1LTU1NmJiN2Q4ZTlmOCIsInJvbGUiOiIifQ.dVQ-YeVtELfotfLikgFpEM2aJnqeZrnbh13RVVVA86M", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))