# Desafio ImpulsoGov: API com FastApi 

Projeto de API com Python criado com o framework [FastAPI](https://pypi.org/project/fastapi/);

O API já está hospedada no [Heroku](https://www.heroku.com/) e pode ser acessada [Clicando Aqui](https://vibrant-baguette-35995.herokuapp.com/);

Ou pode ser instalada para rodar localmente.
  
 ## Instalação e Execução
 
 Para instalação: 
  - clone esse repositório em um repositório local;
  - no terminal navegue até o repositório fast-api e rode comando pip install para instalar todas as dependências necessárias;
```bash
pip install
```

Para execução:

   - abra o terminal e navegue para o repositório fast-api;
   - execute o comando uvicorn main:app --reload;
   - assim que o projeto executar, aparecerá o caminho local aonde estará rodando a API; 
   - normalmente o projeto é executado no caminho http://127.0.0.1:8000/;
   - Pronto! O projeto está rodando localmente;
```bash
uvicorn main:app --reload
```

## End-Points

A API possui duas rotas do tipo GET:

   - [https://vibrant-baguette-35995.herokuapp.com/](https://vibrant-baguette-35995.herokuapp.com/) : retorna apenas um json com message: "server is runnig" ;
   - [https://vibrant-baguette-35995.herokuapp.com/current_time](https://vibrant-baguette-35995.herokuapp.com/current_time) : retorna um json com current_time: "hh:mm" atual;
   - É importante ressaltar que localmente há uma diferença de 3 horas para a hora atual, pois o serviço de hospedagem está com a localização dos Estados Unidos, sendo necessário aplicar uma regra para localização do Brasil;

## Bibliotecas

- [Python](https://www.python.org/)
- [FastAPI framework](https://pypi.org/project/fastapi/)
- [DateTime](https://pypi.org/project/DateTime/#id25)
- [uvicorn](https://pypi.org/project/uvicorn/)
- [gunicorn](https://pypi.org/project/gunicorn/)
- [Heroku](https://www.heroku.com/)
