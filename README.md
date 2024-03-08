# Recomendacao de roupa baseada no clima

Estrutura do Projeto
app.py: Contém a lógica principal do programa.
vestimenta/:
recomendacoes.py: Função para recomendações de vestimenta com base na temperatura e clima.
outros arquivos: Outros módulos ou funções relacionados à vestimenta.
Dependências
requests: Para fazer requisições HTTP à API de clima.
Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas ou enviar pull requests para melhorar este projeto.

Licença
Este projeto é distribuído sob a licença MIT.

Funcionalidades do Projeto
Obtenção de Preferências do Usuário:

O programa solicitará ao usuário informações como orçamento, gênero, estilo, ocasião, cores preferidas, tamanho, tipo de roupas desejadas, material e marcas favoritas.
Essas preferências serão capturadas pela função obter_preferencias_usuario no arquivo recomendacoes.py.
Consulta à API de Clima:

O usuário informará a cidade desejada.
O programa fará uma solicitação à API de clima (OpenWeatherMap) para obter informações sobre temperatura e clima na cidade.
Essa consulta será realizada pela função requests.get em app.py.
Tradução de Dados da API:

As informações retornadas pela API, como temperatura e condição climática, serão traduzidas para o idioma português e as unidades de medida desejadas.
A tradução será feita pelas funções fahrenheit_to_celsius e translate_weather no arquivo recomendacoes.py.
Recomendação de Vestimenta:

Com base na temperatura e condição climática, a função obter_recomendacao_vestimenta em recomendacoes.py fornecerá sugestões de vestimenta adequadas ao clima.
A recomendação será exibida ao usuário após as informações do clima.
Informações Detalhadas sobre Estilo (opcional):

Se o usuário desejar mais informações sobre o estilo escolhido, o programa fornecerá detalhes adicionais.
Essa funcionalidade está integrada à escolha do estilo no processo de obtenção de preferências.
Execução Principal do Programa:

A execução principal do programa ocorrerá no arquivo app.py.
O bloco if __name__ == "__main__": garante que o código dentro dele seja executado apenas quando o script é chamado diretamente.

## Como Usar

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio

2. **Instale as dependencias:**
    ```bash
    pip install -r requirements.txt

2. **Execute o programa:**
    ```bash
    python app.py



