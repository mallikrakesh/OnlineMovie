import requests

url = "https://imdb8.p.rapidapi.com/title/auto-complete"

querystring = {"q":"game of thr"}

headers = {
    'x-rapidapi-host': "imdb8.p.rapidapi.com",
    'x-rapidapi-key': "09ccbe9290msh059a2b4635e0fa8p11b70cjsnbd1dd4bcc1db"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)