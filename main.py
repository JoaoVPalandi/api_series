from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Ola, mundo!"}

@app.get('/item/{item_id}')
async def read_item(item_id: int, q: Optional[str]= None):
    return {"item_id": item_id, "q": q}

@app.get('/soma/{num1}/{num2}')
async def soma(num1: int, num2: int):
    return {"soma": num1 + num2}

@app.get('/sub/{num1}/{num2}')
async def sub(num1: int, num2: int):
    return {"subtração": num1 - num2}

@app.get('/multi/{num1}/{num2}')
async def multi(num1: int, num2: int):
    return {"multiplicação": num1 * num2}

@app.get('/div/{num1}/{num2}')
async def divisao(num1: int, num2: int):
    return {"divisão": num1 // num2}

@app.get('/resto/{num1}/{num2}')
async def resto(num1: int, num2: int):
    return {"resto": num1 % num2}

@app.get('/IMC/{peso}/{altura}')
async def IMC(peso: int, altura: float):
    return {"IMC": peso / (altura * 2)}

@app.get('/parimpar/{num}')
async def parimpar(num: int):
    if num % 2 == 0:
        return {"par"}
    else:
        return {"impar"}


# crie uma rota que retorne a soma de dois números passados por um caminho (path de url)

# extra: melhore a tipagem do codigo usando tipos de módulos typing onde for é necessário