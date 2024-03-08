import requests
from clima.clima_api import api_key
from clima.traducao_clima import translate_weather
from vestimenta.preferencias_user import obter_preferencias_usuario
from vestimenta.recomenda_user import obter_recomendacao_vestimenta
from vestimenta.chatbot import interagir_com_chatbot 
from utils.conversoes import fahrenheit_to_celsius

def main():
    preferencia_user = obter_preferencias_usuario()

    user_input = input("Digite a cidade: ")

    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}"
    )


    #print(weather_data.json())

    if weather_data.json()['cod'] == '404':
        print("Cidade não encontrada")
    else:
        weather = translate_weather(weather_data.json()['weather'][0]['main'])
        temp_fahrenheit = weather_data.json()['main']['temp']
        temp_celsius = fahrenheit_to_celsius(temp_fahrenheit)

        print(f"O clima em {user_input} é: {weather}")
        print(f"A temperatura em {user_input} é: {temp_celsius}ºC")

        recomendacao = obter_recomendacao_vestimenta(temp_celsius, weather)
        print(recomendacao)

if __name__ == "__main__":
    main()