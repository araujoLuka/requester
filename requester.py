# Programa: requester
#
# Objetivo:
#       Facilitar requisicoes HTTP a um determinado IP ou rota
#
# Autor: Lucas Araujo

import os
import requests
import json

def request(url: str, 
            metodo: str = "GET", 
            params: dict = {}, 
            headers: dict = {}) -> requests.Response | None:
    response: requests.Response | None = None
    message: str = "Requisicao nao enviada"
    paramsStr: str = json.dumps(params, indent=4)
    try:
        if metodo == "GET":
            response = requests.get(url, params=paramsStr, headers=headers)
        elif metodo == "POST":
            response = requests.post(url, data=paramsStr, headers=headers)
        else:
            message = f"Metodo '{metodo}' nao suportado"

        if response is None:
            message = "Erro ao enviar requisicao"
            raise Exception(message)

        response.raise_for_status()     # Lanca excecao caso o status code seja diferente de 200

        message = f"Requisicao enviada com sucesso: {response.status_code}"
    except Exception as e:
        message = "Erro: " + str(e)
    finally:
        print(message)
        return response

def urlInput() -> str:
    print("Digite a URL do servidor")
    print(" - Deixe em branco para usar a URL padrao (http://localhost:5000)")
    url: str = input("URL: ")
    
    if url == "":
        url = "http://localhost:5000"
    
    if not url.startswith("http"):
        url = "http://" + url

    if not url.endswith("/"):
        url += "/"

    print(url)
    return url

def pathInput() -> str:
    print("Digite o caminho da rota")
    print(" - Deixe em branco para usar a rota padrao ('/')")
    path: str = input("Caminho: ")

    if path.startswith("/"):
        path = path[1:]

    print(path)
    return path

def metodoInput() -> str:
    print("Escolha o metodo HTTP")
    print(" 1) GET (padrao)")
    print(" 2) POST")
    print(" 3) PUT")
    selStr: str = input("Metodo: ")
    sel: int = 0

    if selStr == "":
        sel = 1

    if selStr.isdigit():
        sel = int(selStr)

    if sel != 0:
        if sel == 1:
            metodo = "GET"
        elif sel == 2:
            metodo = "POST"
        elif sel == 3:
            metodo = "PUT"
        else:
            metodo = "GET"
    else:
        selStr = selStr.upper()
        if sel in ["GET", "POST", "PUT"]:
            metodo = sel
        else:
            raise Exception("Metodo invalido")
    
    print(metodo)
    return metodo

def paramsInput() -> dict:
    print("Qual o tipo de entrada de parametros?")
    print(" 0) Nenhum (padrao)")
    print(" 1) Arquivo JSON")
    print(" 2) JSON via terminal")
    sel: str = input("Tipo: ")
    params: dict = {}

    if sel == "":
        sel = "0"

    if sel == "0":
        return {}
    elif sel == "1":
        params = jsonParamsInput()
    elif sel == "2":
        params = dictParamsInput()
    else:
        raise Exception("Tipo '{}' invalido".format(sel))
    
    return params
    
# input de parametros em JSON (via arquivo)
def jsonParamsInput() -> dict:
    params: dict = {}
    arquivo: str = input("Digite o nome do arquivo: ")
    try:
        with open(arquivo, "r") as file:
            params = json.load(file)
    except Exception as e:
        print("Erro ao abrir arquivo: " + str(e))
    return params

# input de parametros em dicionario (via terminal)
def dictParamsInput() -> dict:
    params: dict = {}
    print("Digite os parametros da requisicao")
    print(" - Digite 'fim' ou deixe em branco para encerrar a insercao")
    while True:
        key: str = input("Chave: ")
        if key == "":
            break
        if key == "fim":
            break
        value: str = input("Valor: ")
        params[key] = value
        print(params)

    if params == {}:
        print("Nenhum parametro inserido")
        return params

    print("Parametros inseridos: ")
    print(json.dumps(params, indent=4))

    confirm: bool = False
    sel: str = input("Confirmar? (s/n): ")
    if sel == "s":
        confirm = True
    elif sel == "n":
        sel = input("Deseja inserir novamente? (s/n): ")
        if sel == "s":
            params = dictParamsInput()
        elif sel == "n":
            confirm = False
    else:
        raise Exception("Opcao invalida")

    if not confirm:
        params = {}
    return params

# input de headers em dicionario (via terminal)
def headersInput() -> dict:
    headers: dict = {}

    # Insere o header 'Content-Type' padrao
    headers["Content-Type"] = "application/json"
    headers["Accept"] = "application/json"

    print("Digite os headers da requisicao")
    print(" - Deixe em branco para nao enviar headers")
    print(" - Digite 'fim' para encerrar a insercao de headers")
    print(" - Para token de autenticacao, digite 'token' no campo chave")
    while True:
        key: str = input("Chave: ")
        if key == "":
            break
        if key == "fim":
            break
        value: str = input("Valor: ")
        # Caso a chave seja 'token', 
        # adiciona o valor ao header 'Authorization'
        if key == "token":
            headers["Authorization"] = "Bearer " + value
            continue
        headers[key] = value
    return headers

if __name__ == "__main__":
    # Verifica se deseja usar a ultima requisicao salva
    lastReq: str = "n"
    if os.path.exists(".last_req.json"):
        lastReq = input("Deseja usar a ultima requisicao salva? (s/n): ")
    if lastReq == "s":
        arquivo: str = ".last_req.json"
        try:
            with open(arquivo, "r") as file:
                req: dict = json.load(file)
            url: str = req["url"]
            path: str = ""
            metodo: str = req["metodo"]
            params: dict = req["params"]
            headers: dict = req["headers"]

        except Exception as e:
            print("Erro ao abrir arquivo: " + str(e))
            input("Pressione qualquer tecla para sair...")
            exit(-1)
    else:
        url: str = urlInput()
        path: str = pathInput()
        metodo: str = metodoInput()
        params: dict = paramsInput()
        headers: dict = headersInput()

    response: requests.Response | None = None
    response = request(url + path, metodo, params, headers)

    if response is None:
        print("Nao foi possivel enviar a requisicao")
        input("Pressione qualquer tecla para sair...")
        exit(1)

    print(response.text)   # Imprime o conteudo da resposta em texto
    # print(response.json()) # Imprime o conteudo da resposta em JSON
        
    save: str = input("Deseja salvar a resposta em um arquivo? (s/n): ")
    if save == "s":
        arquivo: str = input("Digite o nome do arquivo: ")
        with open(arquivo, "w") as file:
            file.write(response.text)
        print("Resposta salva em '{}'".format(arquivo))

    saveReq: str = input("Deseja salvar a requisicao em um arquivo? (s/n): ")
    if saveReq == "s":
        req: dict = {
            "url": url + path,
            "metodo": metodo,
            "params": params,
            "headers": headers
        }
        arquivo: str = ".last_req.json"
        with open(arquivo, "w") as file:
            file.write(json.dumps(req, indent=4))
        print("Requisicao salva em '{}'".format(arquivo))

    input("Pressione qualquer tecla para sair...")
