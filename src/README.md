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

- Build Image: `docker build -t iperoyg/complexop_api:v1.0.0 -f Dockerfile.API .`
- Open Shell: `docker run -it --rm --name api_container iperoyg/complexop_api:v1.0.0 sh`
- Run API:
    - `docker run -d -p 12345:80 --name api_container iperoyg/complexop_api:v1.0.0 uvicorn main:app --host 0.0.0.0 --port 80`
    - `docker run -d --rm -p 12345:80 --env PORT=80 --name api_container iperoyg/complexop_api:v1.0.0`
- Push to registry:
    - `docker push iperoyg/complexop_api:v1.0.0`


## Kubernetes
- kubectl get deploy
- kubectl delete deploy <deployment name>
- kubectl apply -f .\kubernetes_deploy.yml
