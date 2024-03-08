def translate_weather(weather):
    weather_mapping = {
        'Clear': 'Céu limpo',
        'Clouds': 'Nublado',
        'Rain': 'Chuva',
        'Snow': 'Neve',
        'Thunderstorm': 'Tempestade',
        'Mist': 'Neblina',
        
    }
    return weather_mapping.get(weather, weather)