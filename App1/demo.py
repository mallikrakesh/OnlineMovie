import http.client

conn = http.client.HTTPSConnection("imdb8.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "imdb8.p.rapidapi.com",
    'x-rapidapi-key': "4422ecdd22msh0284eaac7d64721p1d830ejsn5fc033392fd1"
    }

conn.request("GET", "/title/auto-complete?q=game%20of%20thr", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))