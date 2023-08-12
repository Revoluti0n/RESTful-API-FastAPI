from fastapi import FastAPI
import requests
import json

# Iniciando o server: uvicorn main:app --reload
# Acessando a API: http://127.0.0.1:8000
# Documentação gerada automaticamente pelo Swagger UI: http://127.0.0.1:8000/docs
# Documentação alternativa gerada pelo ReDoc: http://127.0.0.1:8000/redoc

# Instância a aplicação
app = FastAPI()


@app.get(path='/test')
def hello_root():
    return {'message': 'Hello World!'}


@app.get(path='/')
def web_scraping():
    # URL da API
    url = 'https://servicodados.ibge.gov.br/api/v1/localidades/estados/' \
          '11|12|13|14|15|16|17|21|22|23|24|25|26|27|28|29|31|32|33|35|41|42|43|50|51|52|53' \
          '/municipios'
    # Retorno da API em JSON
    scraped_data_json = requests.get(url=url).text
    # Carrega o JSON
    scraped_data = json.loads(scraped_data_json)
    # Dicionário alvo que será abastecido
    target_dict = {}
    # Listas que serão abastecidas
    target_list = []
    # Para cada dicionário no output da API
    for dictionary in scraped_data:
        # Para cada conjunto chave / valor nos itens desse dicionário
        for key, value in dictionary.items():
            # Abastece o dicionário alvo com as condições definidas
            if key == 'id':
                target_dict['city_id'] = value
            elif key == 'nome':
                target_dict['city_name'] = value
            elif key == 'microrregiao':
                uf = value['mesorregiao']['UF']
                target_dict['uf_id'] = uf['id']
                target_dict['uf_name'] = uf['nome']
                target_dict['uf_acronym'] = uf['sigla']
        # Todos os dicionários organizados em uma lista
        target_list.append(target_dict)
        # Reseta o dicionário
        target_dict = {}

    # Resultado do scraping
    # print(target_list)

    return target_list
