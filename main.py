from fastapi import FastAPI

app = FastAPI()


@app.get(path='/')
def hello_root():
    return {'message': 'Hello World!'}

# Iniciando o server: uvicorn main:app --reload
# Acessando a API: http://127.0.0.1:8000
# Documentação gerada automaticamente pelo Swagger UI: http://127.0.0.1:8000/docs
# Documentação alternativa gerada pelo ReDoc: http://127.0.0.1:8000/redoc
