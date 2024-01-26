# Programa: Requester

Este é um programa em Python chamado `Requester` desenvolvido por Lucas Araujo. O objetivo deste programa é facilitar requisições HTTP a um determinado IP ou rota, oferecendo uma interface simples para o usuário.

## Uso

1. **Execução do Programa:**
   - O programa pode ser executado diretamente a partir do terminal ou do ambiente de desenvolvimento Python.

2. **Interatividade:**
   - O usuário será guiado interativamente para fornecer informações necessárias para a requisição, como URL do servidor, caminho da rota, método HTTP, parâmetros, e cabeçalhos.

3. **Salvamento de Requisições:**
   - O programa oferece a opção de salvar a última requisição em um arquivo `.last_req.json`. Isso permite que o usuário reutilize facilmente as informações da última requisição.

4. **Visualização da Resposta:**
   - A resposta da requisição será exibida no console, mostrando o conteúdo da resposta em texto. O programa também oferece a opção de salvar a resposta em um arquivo.

## Requisitos

- O programa requer Python instalado no ambiente.
- Certifique-se de ter a biblioteca `requests` instalada antes de executar o programa. Você pode instalar a biblioteca utilizando o comando:
  ```bash
  pip install requests
  ```

## Exemplo de Uso

1. Execute o programa.
2. Forneça a URL do servidor.
3. Escolha o caminho da rota.
4. Selecione o método HTTP (GET, POST, ou PUT).
5. Escolha o tipo de entrada de parâmetros (Nenhum, Arquivo JSON, ou JSON via terminal).
6. Insira os parâmetros ou dados, dependendo do método escolhido.
7. Insira os cabeçalhos da requisição.
8. Visualize a resposta da requisição no console.
9. (Opcional) Salve a resposta em um arquivo.
10. (Opcional) Salve as informações da última requisição em um arquivo `.last_req.json`.

**Observação:** Certifique-se de ajustar o programa conforme necessário, especialmente se o servidor esperar um tipo específico de dado no corpo da requisição POST (consulte a seção anterior sobre o erro "Unsupported Media Type").

Este é um exemplo básico de um programa para facilitar requisições HTTP em Python. Sinta-se à vontade para personalizar e expandir conforme necessário para atender aos requisitos específicos do seu projeto.

