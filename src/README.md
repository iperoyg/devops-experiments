# complex operation source

Documentação de `Markdown` para um exemplo:
- Não precisa fazer sentido
- Mas tem que funcionar


**Certo?**

## API
Esse projeto possui uma API baseada em FastAPI. Para executá-la, a partir do raiz do projeto utilize:

`uvicorn --app-dir src\apicomplexoperations main:app --reload`

E abra:

http://127.0.0.1:8000/

## Docker

- Build Image: `docker build -t complexop_iperoyg/api -f Dockerfile.API .`
- Open Shell: `docker run -it --rm --name api_container complexop_iperoyg/api sh`



