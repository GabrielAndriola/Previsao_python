import requests;
from config import API_KEY;

cidade = input('Digite o nome da cidade: ');

link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br";

retorno = requests.get(link).json();

descricao = retorno['weather'][0]['description'];

temperatura = round(retorno['main']['temp'] - 273.15,1); # - 273.15 é pra converter a temperatura

print('A temperatura em '+cidade + ' é: ' + descricao + f" {temperatura} °C");