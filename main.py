import requests
from tkinter import *
from typing import Optional
from config import API_KEY

def busca_temperatura(cidade: str, unidade: Optional[str] = 'Celsius') -> str:
    try:
        link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br"

        retorno = requests.get(link).json()

        # Verifique se o objeto JSON contém a chave "main"
        if 'main' not in retorno:
            raise ValueError("Não foi possível encontrar a temperatura para a cidade especificada.")

        descricao = retorno['weather'][0]['description']

        # Converta a temperatura para a unidade especificada pelo usuário
        if unidade.lower() == 'fahrenheit':
            temperatura = round((retorno['main']['temp'] - 273.15) * 9/5 + 32, 1)
            unidade_str = '°F'
        elif unidade.lower() == 'kelvin':
            temperatura = round(retorno['main']['temp'], 1)
            unidade_str = 'K'
        else:
            temperatura = round(retorno['main']['temp'] - 273.15, 1)
            unidade_str = '°C'

        retorno = f"A temperatura em {cidade.title()} é: {descricao}, {temperatura} {unidade_str}"
        
        return retorno

    except requests.exceptions.RequestException as e:
        return f"Erro de conexão: {e}"
    except (ValueError, KeyError, TypeError) as e:
        return f"Erro: {e}"


def confirmar_click():
    cidade = input_cidade.get()
    unidade = input_unidade.get()

    resultado = busca_temperatura(cidade, unidade)
    retorno_tela.config(text=resultado)


front = Tk()
front.title("Previsão do Tempo")

titulo = Label(front, text='Informe a cidade que deseja saber a temperatura atual:')
titulo.grid(column=0, row=0)

input_cidade = Entry(front)
input_cidade.grid(column=0, row=1)

label_unidade = Label(front, text='Unidade de temperatura (opcional, default = Celsius):')
label_unidade.grid(column=0, row=2)

input_unidade = Entry(front)
input_unidade.grid(column=0, row=3)

b_confirmar = Button(front, text="Confirmar", command=confirmar_click)
b_confirmar.grid(column=0, row=4)

retorno_tela = Label(front, text="")
retorno_tela.grid(column=0, row=5)

front.mainloop()
