import requests

def buscar_lojas_na_cidade(cidade):
    # Chave de API do Google Places (substitua pela sua chave)
    google_places_api_key = 'AIzaSyA7avfR2zZ6K87P21b4_8_8CLWKTCpZCtI'

    # URL da API do Google Places para buscar lojas na cidade
    url = 'https://maps.googleapis.com/maps/api/place/textsearch/json'

    # Parâmetros da requisição
    params = {
        'query': f'lojas de moda em {cidade}',
        'key': google_places_api_key,
    }

    # Fazendo a requisição à API do Google Places
    response = requests.get(url, params=params)

    # Verifica se a requisição foi bem-sucedida (código de status 200)
    if response.status_code == 200:
        # Obtém os resultados da pesquisa
        results = response.json().get('results', [])

        # Lista para armazenar as lojas encontradas
        lojas = []

        # Itera sobre os resultados e extrai informações relevantes
        for result in results:
            loja = {
                'nome': result.get('name', ''),
                'endereco': result.get('formatted_address', ''),
                'cidade': cidade,
            }
            lojas.append(loja)

        return lojas

    else:
        # Em caso de falha na requisição, imprime o código de status
        print(f"Falha na requisição. Código de status: {response.status_code}")
        return None

# Testando a função
cidade_teste = 'Valinhos'  # Substitua pela cidade desejada
lojas_encontradas = buscar_lojas_na_cidade(cidade_teste)

if lojas_encontradas:
    print(f"Lojas encontradas em {cidade_teste}:")
    for loja in lojas_encontradas:
        print(loja)
else:
    print("Falha ao buscar lojas.")
