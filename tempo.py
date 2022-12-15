import requests
import json

url = "https://community-open-weather-map.p.rapidapi.com/find"

querystring = {"q":"itajai, santa catarina","cnt":"3","mode":"null","lon":"0","type":"accurate, like,"lat":"0","units}


headers = {
    'x-rapidapi-key': "ddd6b22bd7msh9dd6e065379016cp180cjsnc0f3dd2ca59e",
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
    }

response = requests.request("GET", url, headers-headers, params=querystring)

#response = requests.get(url, headers, params=querystring)

if (response.status_code == 200):
    nosso_dict = json.loads(response.text)
    nome_cidade = nosso_dict[0]['list']['name']
    temperatura_atual = nosso_dict[0]['list']['main']['temp'] + 'F'
    sensacao_termica = nosso_dict[0]['list']['main']['feels_like'] + 'F'

    print("Cidade", nome_cidade, "sensação", sensacao_termica, "temperatura", temperatura_atual)
    

else:
    print("falha")

